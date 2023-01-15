import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\Train.csv")

df.set_index('PassengerId')
print(df)

print(df.isnull().sum())

print(df.Sex.value_counts())
