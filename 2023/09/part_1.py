# Day 9: Mirage Maintenance - Part One

import pandas as pd
from sklearn.linear_model import LinearRegression

file = pd.read_csv('input.txt', header=None, sep=' ')

X = file.iloc[:,:-1]
y = file.iloc[:,-1]

reg = LinearRegression().fit(X, y)

X = file.iloc[:,1:] 
pred = reg.predict(X)

pred = list(map(round, pred))

print(sum(pred)) #1939607039
