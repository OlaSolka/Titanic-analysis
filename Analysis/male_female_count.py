import pandas as pd

# This short calculation shows how many of the passengers were male and female.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

print(df.Sex.value_counts())

# It's quite simple. There were significantly more men than women.
