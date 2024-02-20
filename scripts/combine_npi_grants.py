import pandas as pd
from DUQ330BIGDATA.Week2 import read_data_exp 
from DUQ330BIGDATA.Week5 import npi_reader


def read(path: str, path2: str) -> pd.DataFrame:
    """
    This function takes in 2 dataframe paths and returns a concatenated dataframe

    Args:
    path -> path of file grants
    path2 -> seconf file path npi

    Return:
    A Pandas DataFrame
    """

    gd = read_data_exp.GrantsData(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\RePORTER_PRJ_C_FY2022.zip")
    df = gd.read()
    df2 = npi_reader.read(path2)

    df = df[['forename', 'last_name', 'city', 'state', 'country']]
    df2 = df2[['forename', 'last_name', 'city', 'state', 'country']]

    mapper = {
            'forename': 'grant_forename',
            'last_name': 'grant_last_name',
            'city': 'grant_city',
            'state': 'grant_state',
            'country': 'grant_country',
        }
    
    mapper2 = {
            'forename': 'npi_forename',
            'last_name': 'npi_last_name',
            'city': 'npi_city',
            'state': 'npi_state',
            'country': 'npi_country',
        }

    
    df = df.rename(columns=mapper)[mapper.values()]
    df2 = df2.rename(columns=mapper2)[mapper.values()]

    df_final = pd.concat(df, df2, axis=1)

    return df_final


if __name__ == '__main__':
    df = read( r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\RePORTER_PRJ_C_FY2022.csv", r"data/npidata_pfile_20240205-20240211.csv")
    print(df.head())