import matplotlib.pyplot as plt
import pandas as pd

# This simple pie chart shows gender breakdown.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

explode = (0.05, 0.05)
colors = ["steelblue", "pink"]
df.Sex.value_counts().plot(kind='pie', y='Sex', autopct='%0.1f%%', colors=colors, explode=explode)
plt.show()

# Almost 65% of passengers were male. Slightly over 35% were female.
