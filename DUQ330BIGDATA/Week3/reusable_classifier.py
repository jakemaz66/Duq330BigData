import pandas as pd
from sklearn.model_selection import train_test_split
import datetime
import numpy
import os
import json
import xgboost as xgb

#Camel Case because it's a class
class ReusableClassifier():

    def __init__(self, model_dir, model):
        """
        Constructor

        Args:
        model is the type of classifier we are loading
        model_dir is the directory in which to save the model
        """

        #Initialize model in __init__
        self.model = (self._initialize_xgb_model() if model == 'xgb' 
                      else self._initialize_random_forests())
        self.metadata = {}
        self.model_dir = model_dir

    def train(self, features: pd.DataFrame, labels: pd.Series):
        """
        Train the classifier on the data

        Args:
        features: The feature columns of the dataset
        labels: The column that is to be predicted
    
        """

        #Test size can go down as training data goes up
        features, features_test, labels, labels_test = train_test_split(features, labels, test_size=0.2)

        self.model.fit(features, labels)

        self.metadata['training_date'] = datetime.datetime.now().strftime()('%y%m%d')
        self.metadata['training_rows'] = len(labels)

        self.metadata['accuracy'] = self.asses(features_test, labels_test)

        

    def predict(self, features: pd.DataFrame, proba: bool = False) -> numpy.ndarray:
        """
        Model predicts on the test_data

        Args:
        features: the features of the dataset
        proba: whether to return probabilities

        Returns:
        numpy array 
        """
        if len(self.metadata) == 0:
            raise ValueError("Model must be trained first")

        if proba:
             return self.model.predict_proba(features)[:, 0]
        return self.model.predict(features)
    
    def save(self, file_name: str, overwrite: bool = False):
        """
        Save to location path on hard drive

        Args:
        file_name: the name of the file to save
        overwrite: a boolean to check for permission to overwrite an existing file_name
        """

        if len(self.metadata) == 0:
            raise ValueError("Model must be trained before saving")
        
        now = datetime.datetime.now().strftime()('%y%m%d')
        
        if file_name[:6] != now:
            filename = f'{now}_{file_name}'

        #Check for correct file suffix
        if os.path.splittext(file_name)[1] != 'json':
            file_name = file_name + '.json'
        
        #Pickle is dangerous because it depends on correct versioning
            
        if not overwrite and (os.path.exists(path) or os.path.exists(metadata_path)):
            raise FileExistsError("Cannot overwrite existing file")
        
        path = os.path.join(self.model_dir, file_name)
        metadata_path = os.path.splittext(path)[0] + '_metadata.json'
                            
        self.model.save_model(path)

        with open(metadata_path) as fo:
            json.dump(self.metadata, fo)


    def load(self, file_name):
        """
        load in a model filename with associated metadata from model_dir

        Args:
        file_name: name of the model file
        """

        path = os.path.join(self.model_dir, file_name)
        metadata_path = os.path.splittext(path)[0] + '_metadata.json'

        self.model.load_model(path)
        with open(metadata_path) as fo:
            json.dump(self.metadata, fo)
        

    def assess(self, features, labels) -> float:
        """
        Returns the accuracy of the model

        Args:
        features: The feature columns of the dataset
        labels: The column that is to be predicted

        Returns:
        Accuracy of model chosen metric
        
        """

        #Calculating Accuracy
        pred_labels = self.predict(features)
        return ((pred_labels == labels).sum() / len(labels))
    
    def _initialize_xgb_model():
        """Create a new xgbclassifier"""
        return xgb.XGBClassifier()
    