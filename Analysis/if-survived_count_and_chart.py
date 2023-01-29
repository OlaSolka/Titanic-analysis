import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# In this part of the analysis I want to see how many people actually survived the Titanic catastrophe.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df.loc[:, "Survived"][df.Survived == 0] = "no"
df.loc[:, "Survived"][df.Survived == 1] = "yes"

print(df.Survived.value_counts())

sbn.catplot(data=df, x='Survived', kind='count')
plt.show()

# As we can see from this short analysis, the majority of passengers didn't survive the catastrophe. Actually
# less than 40% didn't die.
