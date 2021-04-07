import pandas as pd 

wine_red=["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]
pwine_red= pd.read_csv('第十二次上机\\winequality-red.csv',sep=';',names=wine_red)
print(pwine_red)