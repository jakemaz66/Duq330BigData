from DUQ330BIGDATA.Week5 import distance_classifier, distances, npi_grants_combine
from DUQ330BIGDATA.Week5 import npi_grants_combine


model = distance_classifier.DistanceClassifier('DUQ330BIGDATA/Week6', 'xgb')
model.load('distance_classifier.json')

test_data = npi_grants_combine.read(r"data/npidata_pfile_20240205-20240211.csv")
test_data = test_data.iloc[0:100]
features = distances.NameDistance().training_data(test_data)

preds = model.predict(features)
