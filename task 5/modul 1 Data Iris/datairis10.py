import pandas as pd 

df = pd.read_csv("iris.csv")
df["petalLengthCm"].mean()