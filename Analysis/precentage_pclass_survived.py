import pandas as pd

# Here, I want to check how ticket class impacts the survival rate.

df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")

class1 = df["Survived"][df["Pclass"] == 1].value_counts(normalize=True)[1]*100
first_class = round(class1, 2)
print(f"Percentage of first class passengers who survived: {first_class}")

class2 = df["Survived"][df["Pclass"] == 2].value_counts(normalize=True)[1]*100
second_class = round(class2, 2)
print(f"Percentage of second class passengers who survived: {second_class}")

class3 = df["Survived"][df["Pclass"] == 3].value_counts(normalize=True)[1]*100
third_class = round(class3, 2)
print(f"Percentage of third class passengers who survived: {third_class}")

# We can clearly see thatMajority of first class passengers survived. A little less that 50% of second class passengers
# also survived. But the majority of the third class passengers didn't make it. Now, I can only speculate what was the
# reason that more wealthy people survived. Maybe because their cabins were closer to the rescue boats, and so they
# could be there quicker. But there's the other side. Maybe, they knew earlier that the rest and the ship crew took care
# of them first, because of their status.
