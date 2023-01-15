import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df['Age'].plot(kind='hist', bins=20, color='grey')
plt.show()
