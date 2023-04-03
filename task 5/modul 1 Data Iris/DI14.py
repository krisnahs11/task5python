import pandas as pd 

df = pd.read_csv("iris.csv")
dfValueCountsPetalLengthCm= df["PetalLengthCm"].value_counts().rename_axis('SPetalLengthCm Value Counts').reset_index(name='Counts')
dfValueCountsPetalLengthCm