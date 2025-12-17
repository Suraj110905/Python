#coficent.py
import pandas
from sklearn import linear_model

df = pandas.read_csv(r
                     "C:\Users\Lenovo\OneDrive\Desktop\python\PPC-python\MACHINE LEARNING\cardata.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

print(regr.coef_)