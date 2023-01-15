import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\Train.csv")

explode = (0.05, 0.05)
colors = ["steelblue", "pink"]
df.Sex.value_counts().plot(kind='pie', y='Sex', autopct='%1.0f%%', colors=colors, explode=explode)
plt.show()
