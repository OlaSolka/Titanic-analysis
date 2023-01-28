import pandas as pd

# Here I check how the percentage of passengers that have siblings ang survived look against those who don't have
# siblings.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

zero = df["Survived"][df["SibSp"] == 0].value_counts(normalize=True)[1]*100
zero_siblings = round(zero, 2)
print(f"Percentage of passengers with no siblings who survived:{zero_siblings}")

one = df["Survived"][df["SibSp"] == 1].value_counts(normalize=True)[1]*100
one_sibling = round(one, 2)
print(f"Percentage of passengers with one sibling who survived:{one_sibling}")

two = df["Survived"][df["SibSp"] == 2].value_counts(normalize=True)[1]*100
two_siblings = round(two, 2)
print(f"Percentage of passengers with two siblings who survived:{two_siblings}")

# Results show that passengers who had siblings were more likely to survive. I assume that it was easier to run and
# search for safe place with someone's help. The nearest company was family and that's why having siblings helped to
# survive the catastrophe.
