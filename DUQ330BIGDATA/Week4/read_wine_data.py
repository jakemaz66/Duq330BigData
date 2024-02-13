import pandas as pd

def read(path):
    path = r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\winequality-red.csv"

    df = pd.read_csv(path, delimiter=';')
    return df

if __name__ == '__main__':
    read(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\winequality-red.csv")

#classifier = AuthorDoctorEntityResolver()




