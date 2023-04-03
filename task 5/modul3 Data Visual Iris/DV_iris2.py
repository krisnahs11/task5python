import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(color_codes=true)

import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("iris.csv")

df.plot(kind="scatter", x="SepallengthCm", y="SepalWidthCm")