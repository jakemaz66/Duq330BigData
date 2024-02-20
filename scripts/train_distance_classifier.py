from DUQ330BIGDATA.Week5 import npi_reader, distance_classifier, distances
from DUQ330BIGDATA.Week2 import read_data_exp 

#NPI Data
npi_df = npi_reader.read(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\npidata_pfile_20240205-20240211.csv")

#Grants Data
gd = read_data_exp.GrantsData()
grants_df = gd.read(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\RePORTER_PRJ_C_FY2022.zip")

nd = distances.NameDistance()
nd.training_data()


dc = distance_classifier.DistanceClassifier(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week4", 'data')

#dc.train(df)
#dc.save('distance_classifier')