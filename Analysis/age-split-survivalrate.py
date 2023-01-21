import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df["Age"] = df["Age"].fillna(-0.5)

bins =[-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df["Age"], bins, labels = labels)
df['AgeGroup'] = pd.cut(df["Age"], bins, labels = labels)
print(df)
#draw a bar plot of Age vs. survival
sbn.barplot(x="AgeGroup", y="Survived", data=df)
plt.show()
