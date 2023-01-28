import pandas as pd

# Here, I want to check how ticket class impacts the survival rate.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

class1 = df["Survived"][df["Pclass"] == 1].value_counts()[1]
print(f"Number of first class passengers who survived: {class1}")

class2 = df["Survived"][df["Pclass"] == 2].value_counts()[1]
print(f"Number of second class passengers who survived: {class1}")

class3 = df["Survived"][df["Pclass"] == 3].value_counts()[1]
print(f"Number of third class passengers who survived: {class3}")
