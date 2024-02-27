import pandas as pd

#Creating simulated dataframe
df = pd.DataFrame(columns=['grant_forename',
                           'grant_last_name',
                            'grant_city',
                            'grant_state',
                            'grant_country',
                            'npi_forename',
                            'npi_last_name',
                            'npi_city',
                            'npi_state',
                            'npi_country',
                            'label'])

#Label 1 is a match label 0 is not a match
df.loc[len(df)] = {'grant_forename': 'Arthur', 
           'grant_last_name': 'Smith', 
           'grant_city': 'Memphis', 
           'grant_state': 'MO', 
           'grant_country': 'USA', 
           'npi_forename': 'Arthur', 
           'npi_last_name': 'Smith Jr', 
           'npi_city': 'Memphis', 
           'npi_city': 'MO', 
           'npi_country': 'USA', 
           'label': 1}

df.loc[len(df)] = {'grant_forename': 'Anthony', 
           'grant_last_name': 'Smith', 
           'grant_city': 'Memphis', 
           'grant_state': 'MO', 
           'grant_country': 'USA', 
           'npi_forename': 'Arthur', 
           'npi_last_name': 'Smith Jr', 
           'npi_city': 'Memphis', 
           'npi_city': 'MO', 
           'npi_country': 'USA', 
           'label': 0}

df.loc[len(df)] = {'grant_forename': 'Anthony', 
           'grant_last_name': 'Jones', 
           'grant_city': 'Pittsburgh', 
           'grant_state': 'MO', 
           'grant_country': 'USA', 
           'npi_forename': 'Arthur', 
           'npi_last_name': 'Smith Jr', 
           'npi_city': 'Memphis', 
           'npi_city': 'MO', 
           'npi_country': 'USA', 
           'label': 0}

print(df.head())