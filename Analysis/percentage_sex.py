import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

print("Percentage of male passengers who survived:",
      df["Survived"][df["Sex"] == "male"].value_counts(normalize=True)[1]*100)

print("Percentage of female passengers who survived:",
      df["Survived"][df["Sex"] == "female"].value_counts(normalize=True)[1]*100)
