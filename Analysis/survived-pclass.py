import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Here I made a bar chart of the survival rate in each ticket class.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df.loc[:, "Survived"][df.Survived == 0] = "no"
df.loc[:, "Survived"][df.Survived == 1] = "yes"

sns.catplot(data=df, x='Pclass', kind='count', hue='Survived')
plt.show()

# There is clear correlation between ticket class and survival. Clearly, wealthier people were treated better or were
# located better in case of any emergency. Maybe the crew was told that they should take care of the richer
# first and that the rest.
