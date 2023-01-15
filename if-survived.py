import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\Train.csv")

df.loc[:, "Survived"][df.Survived == 0] = "no"
df.loc[:, "Survived"][df.Survived == 1] = "yes"

sns.catplot(data=df, x='Survived', kind='count')
plt.show()
