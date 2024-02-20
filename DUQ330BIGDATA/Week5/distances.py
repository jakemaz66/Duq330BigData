import fasttext
import numpy
import pandas as pd
import jarowinkler

class NameDistance():

    def __init__(self, ft_model_path):
        self.ft_model_path = fasttext.load_model(ft_model_path)

    def training_data(self, df: pd.DataFrame) -> pd.DataFrame:
        #Grants data has
        #last_name, forename, city, state, country
        #NPI Data has
        #last_name, firstname, city, state, country
        #Prefix of grant_ or npi_

        data_cols = df.columns


        df['jw_dist_last_name'] = df.apply(lambda row: jarowinkler.jaro_similarity(row['grant_last_name'], row['npi_last_name']), axis=1)

        df['jw_dist_forename'] = df.apply(lambda row: jarowinkler.jaro_similarity(row['grant_forename'], row['npi_forename']), axis=1)

        df['match_city'] = df.apply(lambda row: row['grant_city'] == row['npi_city'], axis=1)
        df['match_state'] = df.apply(lambda row: row['grant_state'] == row['npi_state'], axis=1)


        for dataset in ['grant', 'npi']:
            for col in ['last_name', 'forename']:

                df[f'vec_{dataset}_{col}'] =  df[f'vec_{dataset}_{col}'].apply(lambda x: self.ft_model.get_sentence_vector(x))

        df['ft_dist_last_name'] = df.apply(lambda row: numpy.linalg.norm(row['vec_grant_last_name'] - row['vec_npi_last_name']), axis=1)


        return df.drop(columns=data_cols).drop(columns=[v for v in df.columns if 'vec_' in v])
    
    #Pass the output of this into a new classifier model from reusable classifier, train the classifier




    