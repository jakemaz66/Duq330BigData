from DUQ330BIGDATA.Week5 import npi_reader, distance_classifier, distances, npi_grants_combine
from DUQ330BIGDATA.Week2 import read_data_exp 

#Data
data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")


nd = distances.NameDistance()
df = nd.training_data(data)


dc = distance_classifier.DistanceClassifier(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week4", 'data')

dc.train(df)
dc.save('distance_classifier')