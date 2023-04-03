import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set(color_codes=true)

import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("iris.csv")

sns.jointplot(x="SepallengthCm", y="SepalWidthCm", data=df, size=5)