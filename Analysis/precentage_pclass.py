import pandas as pd

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

print("Percentage of first class passengers who survived:",
      df["Survived"][df["Pclass"] == 1].value_counts(normalize=True)[1]*100)

print("Percentage of second class passengers who survived:",
      df["Survived"][df["Pclass"] == 2].value_counts(normalize=True)[1]*100)

print("Percentage of third class passengers who survived:",
      df["Survived"][df["Pclass"] == 3].value_counts(normalize=True)[1]*100)
