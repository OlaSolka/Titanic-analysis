import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

# Here is the part of the analysis showing the survival rate for a specific age group. I'm considering that there will
# be some empty spots in the file. Therefore, I'm adding the 'unknown' category. After that we have Baby, Child,
# Teenager, Student, Young Adult, Adult and Senior.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df["Age"] = df["Age"].fillna(-0.5)

bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
print(df['AgeGroup'].value_counts())
sbn.barplot(x="AgeGroup", y="Survived", data=df)
plt.show()

# This short analysis shows that children are more likely to survive. The lower age the greater chance of survival.
# It probably results from the "women and children first" statement.
