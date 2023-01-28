import pandas as pd
df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

male_survived = df["Survived"][df["Sex"] == "male"].value_counts()[1]
print(f"Number of male passengers who survived: {male_survived}")

female_survived = df["Survived"][df["Sex"] == "female"].value_counts()[1]
print(f"Number of female passengers who survived: {female_survived}")

male_notsurvived = df["Survived"][df["Sex"] == "male"].value_counts()[0]
print(f"Number of male passengers who didn't survived: {male_notsurvived}")

female_notsurvived = df["Survived"][df["Sex"] == "female"].value_counts()[0]
print(f"Number of female passengers who didn't survived: {female_notsurvived}")
