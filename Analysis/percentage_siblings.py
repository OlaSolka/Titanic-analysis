import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

print("Percentage of passengers with no siblings who survived:",
      df["Survived"][df["SibSp"] == 0].value_counts(normalize = True)[1]*100)

print("Percentage of passengers with one sibling who survived:",
      df["Survived"][df["SibSp"] == 1].value_counts(normalize = True)[1]*100)

print("Percentage of passengers with two siblings who survived:",
      df["Survived"][df["SibSp"] == 2].value_counts(normalize = True)[1]*100)
