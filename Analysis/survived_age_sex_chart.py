import seaborn as sbn
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# On this plot i want to see the distribution of Age against gender and with the division into survived/ not survived.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df.loc[:, "Survived"][df.Survived == 0] = "no"
df.loc[:, "Survived"][df.Survived == 1] = "yes"

sbn.displot(data=df, x=df['Age'], hue=df['Sex'], col=df['Survived'])
plt.show()

# First of all, we can see that men on the ship were much older than women. Also in almost every Age group more woman
# survived. Only exceptions to this rule are the youngest: babies and children, and the oldest. Most of the Adult men
# was called to help the ship crew, so they had significantly less chance of survival.
