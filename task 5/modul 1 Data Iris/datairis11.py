import pandas as pd 

df = pd.read_csv("iris.csv")
df["sepalWidthCm"].min()