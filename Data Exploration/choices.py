import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import warnings
warnings.filterwarnings('ignore')

class Choices:
    """Class that includes two choices. User can pick either graphs - 1 or statistics - 2.
    Depending on the choice you can use different method"""

    df = pd.read_csv(
            r"C:\Users\solka\PycharmProjects\Titanic-Analysis\train.csv", on_bad_lines='skip')

    def __init__(self, df):
        self.df = df

    def choice2(self):
        """If user picked graphs this functions shows a list of choices.
        User can choose what data they want to see in the form of chart."""

        df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\train.csv")
        choice2 = int(
            input("What do you want to do? Type corresponding number.\n 1. Woman/man split\n 2. Survived/not survived"
                  "\n 3. Gender against survival rate\n 4. Age groups against survival\n "
                  "5. Survival rate against ticket class\n 6. If survived in different age groups - gender split\n"))

        if choice2 == 1:
            explode = (0.05, 0.05)
            colors = ["steelblue", "pink"]
            df.Sex.value_counts().plot(kind='pie', y='Sex', autopct='%0.1f%%', colors=colors, explode=explode)
            print(plt.show())
        elif choice2 == 2:
            df.loc[:, "Survived"][df.Survived == 0] = "no"
            df.loc[:, "Survived"][df.Survived == 1] = "yes"
            sbn.catplot(data=df, x='Survived', kind='count')
            plt.show()
        elif choice2 == 3:
            df.loc[:, "Survived"][df.Survived == 0] = "no"
            df.loc[:, "Survived"][df.Survived == 1] = "yes"
            sbn.catplot(data=df, x='Sex', hue='Survived', kind='count')
            plt.show()
        elif choice2 == 4:
            df["Age"] = df["Age"].fillna(-0.5)
            bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
            labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
            df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
            sbn.barplot(x="AgeGroup", y="Survived", data=df)
            plt.show()
        elif choice2 == 5:
            df.loc[:, "Survived"][df.Survived == 0] = "no"
            df.loc[:, "Survived"][df.Survived == 1] = "yes"
            sbn.catplot(data=df, x='Pclass', kind='count', hue='Survived')
            plt.show()
        elif choice2 == 6:
            df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis/train.csv")
            df.loc[:, "Survived"][df.Survived == 0] = "no"
            df.loc[:, "Survived"][df.Survived == 1] = "yes"
            sbn.displot(data=df, x=df['Age'], hue=df['Sex'], col=df['Survived'])
            plt.show()
        else:
            print("Invalid input. Try again.")


    def choice3(self):
        """If user picked graphs this functions shows a list of choices.
                User can choose what data they want to see in the form of chart."""

        df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\train.csv")
        choice3 = int(
            input("What do you want to do? Type corresponding number.\n 1. Woman/man split\n 2. Survived/not survived"
                  "\n 3. Gender against survival rate\n 4. Age groups count. \n "
                  "5. Survival rate against ticket class\n 6. Percentage of survivors having siblings onboard \n"))

        if choice3 == 1:
            print(df.Sex.value_counts())
        elif choice3 == 2:
            print(df.Survived.value_counts())
        elif choice3 == 3:
            male_survived = df["Survived"][df["Sex"] == "male"].value_counts()[1]
            female_survived = df["Survived"][df["Sex"] == "female"].value_counts()[1]
            male_notsurvived = df["Survived"][df["Sex"] == "male"].value_counts()[0]
            female_notsurvived = df["Survived"][df["Sex"] == "female"].value_counts()[0]
            print(f"Number of male passengers who survived: {male_survived}")
            print(f"Number of female passengers who survived: {female_survived}")
            print(f"Number of male passengers who didn't survived: {male_notsurvived}")
            print(f"Number of female passengers who didn't survived: {female_notsurvived}")
        elif choice3 == 4:
            df["Age"] = df["Age"].fillna(-0.5)
            bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
            labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
            df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
            print(df['AgeGroup'].value_counts())
        elif choice3 == 5:
            class1 = df["Survived"][df["Pclass"] == 1].value_counts()[1]
            print(f"Number of first class passengers who survived: {class1}")
            class2 = df["Survived"][df["Pclass"] == 2].value_counts()[1]
            print(f"Number of second class passengers who survived: {class2}")
            class3 = df["Survived"][df["Pclass"] == 3].value_counts()[1]
            print(f"Number of third class passengers who survived: {class3}")
        elif choice3 == 6:
            zero = df["Survived"][df["SibSp"] == 0].value_counts(normalize=True)[1] * 100
            zero_siblings = round(zero, 2)
            print(f"Percentage of passengers with no siblings who survived:{zero_siblings}")
            one = df["Survived"][df["SibSp"] == 1].value_counts(normalize=True)[1] * 100
            one_sibling = round(one, 2)
            print(f"Percentage of passengers with one sibling who survived:{one_sibling}")
            two = df["Survived"][df["SibSp"] == 2].value_counts(normalize=True)[1] * 100
            two_siblings = round(two, 2)
            print(f"Percentage of passengers with two siblings who survived:{two_siblings}")
        else:
            print("Invalid input. Try again.")
