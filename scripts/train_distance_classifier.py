from DUQ330BIGDATA.Week5 import distance_classifier, distances, npi_grants_combine

#Obtaining data using npi_grants_combine reacer file
data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")

#Making training data by instantiating NameDistance Class and making features
nd = distances.NameDistance()
df = nd.training_data(data)

#Creating a classifier
dc = distance_classifier.DistanceClassifier(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week4", 'data')

#Training and saving the model
dc.train(df)
dc.save('distance_classifier')