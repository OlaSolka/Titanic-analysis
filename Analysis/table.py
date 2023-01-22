import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

df.set_index('PassengerId')
print(df)

# This line of code prints the data for me.
