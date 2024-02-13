import pandas as pd

def read(path):
    path = path

    df = pd.read_csv(path)

    mapper = {
            'NPI': 'npi',
            'Provider Last Name (Legal Name)': 'last_name',
            'Provider First Name': 'first_name',
            'Provider First Line Business Mailing Address': 'address',
            'Certification Date': 'cert_date'
        }
    
    df = df.rename(columns=mapper)[mapper.values()]

    return df

if __name__ == '__main__':
    df = read(r"data/npidata_pfile_20240205-20240211.csv")
    print(df.head())