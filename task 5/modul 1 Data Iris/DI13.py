import pandas as pd 

df = pd.read_csv("iris.csv")
dfValueCountsSpecies= df["Species"].value_counts().rename_axis('Species Value Counts').reset_index(name='Counts')
dfValueCountsSpecies