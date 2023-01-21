import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df.loc[:, "Survived"][df.Survived == 0] = "no"
df.loc[:, "Survived"][df.Survived == 1] = "yes"

sns.catplot(data=df, x='Pclass', kind='count', hue='Survived')
plt.show()
