from DUQ330BIGDATA.Week4 import read_wine_data, wine_classifier

df = read_wine_data.read(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\data\winequality-red.csv")

wc = wine_classifier.WineClassifier(r"C:\Users\jakem\OneDrive\Documents\Visual Studio 2017\Duq330BigData\DUQ330BIGDATA\Week4", 'data')

wc.train(df.drop(columns=['quality']), df['quality'])
wc.save('wine_classifier')

