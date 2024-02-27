from DUQ330BIGDATA.Week5 import distance_classifier, distances, npi_grants_combine
from DUQ330BIGDATA.Week6 import data_simulator, distance_features
from DUQ330BIGDATA.Week2 import read_data_exp
from DUQ330BIGDATA.Week5 import npi_grants_combine
import json


model = distance_classifier.DistanceClassifier(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week6", 'data')
model.load(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week6\distance_classifier.json")



test_data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")
test_data = test_data.iloc[0:100]
features = distance_features.StringDistanceFeatures().features_from_pairs(test_data)

model.predict(features)
