import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(color_codes=true)

import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("iris.csv")

sns.FaceGrid(df, hue="species", palette="hls", size=5) \
    .map(plt.scatter, "SepallengthCm", "SepalWidthCm") \
    .add_legend()    

sns.FaceGrid(df, hue="species", palette="set2", size=5) \
    .map(plt.scatter, "SepallengthCm", "SepalWidthCm") \
    .add_legend()        

sns.FaceGrid(df, hue="species", palette="cubehelix", size=5) \
    .map(plt.scatter, "SepallengthCm", "SepalWidthCm") \
    .add_legend()    