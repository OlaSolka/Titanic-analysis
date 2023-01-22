import matplotlib.pyplot as plt
import pandas as pd

# Histogram that shows how the age of passengers is distributed across population.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df['Age'].plot(kind='hist', bins=20, color='grey')
plt.show()

# In the plot we can se that it is almost normal distribution except the one extreme value which is the youngest group.
# The largest group is between 20 and 40 years old.
