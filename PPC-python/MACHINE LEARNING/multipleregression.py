#multipleregression.py
import pandas
from sklearn import linear_model

df = pandas.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\python\PPC-python\MACHINE LEARNING\cardata.csv")

X = df[['Weight', 'CO2']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)


#predict the CO2 emission of a car where the weight is 2300g, and the volume is 1300ccm:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)