import pandas as pd

# For the better understanding of the data, I need to be aware of the lacks of data.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

print(df.isnull().sum())

# As the numbers show, there are a lot of lacks of data in the "Age" column as well as the "Cabin".
