import pandas as pd 

df = pd.read_csv('iris_unclean.csv')
df2 = pd.DataFrame({'SepalLengthCm' : dfDataBaru, 'SepalWidthCm' : df['SepalWidthCm'],
                    'PetalLengthCm' : df['PetalLengthCm'], 'PetalLengthCm' : df['PetalLengthCm'], 
                    'Species' : df['Species']})