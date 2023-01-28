import pandas as pd

# Here is the percentage of passengers from each gender that survived the catastropy.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

malesurvived = df["Survived"][df["Sex"] == "male"].value_counts(normalize=True)[1]*100
male_survived = round(malesurvived, 2)
print(f"Percentage of male passengers who survived: {male_survived}")

femalesurvived = df["Survived"][df["Sex"] == "female"].value_counts(normalize=True)[1]*100
female_survived = round(femalesurvived, 2)
print(f"Percentage of female passengers who survived: {female_survived}")

# It's easily noticeable that significantly more men died. I assume that it's because of the cultural standard that
# men should protect women, so women can take care of children. Therefore, men stayed for longer on the drowning ship
# and were more likely to die.
