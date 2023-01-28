import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Chart of the survival against gender.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df.loc[:, "Survived"][df.Survived == 0] = "no"
df.loc[:, "Survived"][df.Survived == 1] = "yes"

sbn.catplot(data=df, x='Sex', hue='Survived', kind='count')
plt.show()

# On this chart we can see that there's fewer women that didn't survive that men that survived. This is interesting
# because, we can assume that the cultural background had huge impact on that. Men taking care of the rest is such a
# big thing, so they actually risked their lives.
