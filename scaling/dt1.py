import pandas

df = pandas.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\python\scaling\LOAN.csv")


d = {'Urban': 0, 'Rural': 1, 'Semiurban': 2}
df['Property_Area'] = df['Property_Area'].map(d)
d = {'Y': 1, 'N': 0}
df['Loan_Status'] = df['Loan_Status'].map(d)
d = {'Graduate':5, 'Not Graduate':8}
df['Education'] = df['Education'].map(d)
d = {'Yes':2, 'No':3}
df ['Married']= df['Married'].map(d)

print(df)