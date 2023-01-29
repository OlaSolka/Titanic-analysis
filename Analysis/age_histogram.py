import matplotlib.pyplot as plt
import pandas as pd

# Histogram that shows how the age of passengers is distributed across population.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df['Age'].plot(kind='hist', bins=20, color='grey')
# df["Age"] = df["Age"].fillna(-0.5)
#
# bins = [-1, 0, 5, 12, 18, 24, 35, 60, 100]
# labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
# df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
# df['AgeGroup'].plot(kind='hist', bins=bins, labels=labels)
plt.show()

# In the plot we can se that it is almost normal distribution except the one extreme value which is the youngest group.
# The largest group is between 20 and 40 years old.
