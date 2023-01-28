import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
import warnings
from art import logo
warnings.filterwarnings('ignore')

print(logo)

print("Hi, welcome to the titanic catastrophe data exploration!")

should_continue = True

while should_continue:

    df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\train.csv")

    choice = int(input("What do you want to generate? Type '1' for graph or '2' for numbers\n"))

    choice2 = int(
        input("What do you want to do? Type corresponding number.\n 1. Woman/man split\n 2. Survived/not survived"
              "\n 3. Gender against survival rate\n 4. Age groups against survival\n "
              "5. Survival rate against ticket class\n"))

    if (choice == 1) and (choice2 == 1):
        explode = (0.05, 0.05)
        colors = ["steelblue", "pink"]
        df.Sex.value_counts().plot(kind='pie', y='Sex', autopct='%0.1f%%', colors=colors, explode=explode)
        print(plt.show())
    elif (choice == 1) and (choice2 == 2):
        df.loc[:, "Survived"][df.Survived == 0] = "no"
        df.loc[:, "Survived"][df.Survived == 1] = "yes"
        sbn.catplot(data=df, x='Survived', kind='count')
        plt.show()
    elif (choice == 1) and (choice2 == 3):
        df.loc[:, "Survived"][df.Survived == 0] = "no"
        df.loc[:, "Survived"][df.Survived == 1] = "yes"
        sbn.catplot(data=df, x='Sex', hue='Survived', kind='count')
        plt.show()
    elif (choice == 1) and (choice2 == 4):
        df["Age"] = df["Age"].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
        sbn.barplot(x="AgeGroup", y="Survived", data=df)
        plt.show()
    elif (choice == 1) and (choice2 == 5):
        df.loc[:, "Survived"][df.Survived == 0] = "no"
        df.loc[:, "Survived"][df.Survived == 1] = "yes"
        sbn.catplot(data=df, x='Pclass', kind='count', hue='Survived')
        plt.show()
    elif (choice == 2) and (choice2 == 1):
        print(df.Sex.value_counts())
    elif (choice == 2) and (choice2 == 2):
        print(df.Survived.value_counts())
    elif (choice == 2) and (choice2 == 3):
        male_survived = df["Survived"][df["Sex"] == "male"].value_counts()[1]
        female_survived = df["Survived"][df["Sex"] == "female"].value_counts()[1]
        male_notsurvived = df["Survived"][df["Sex"] == "male"].value_counts()[0]
        female_notsurvived = df["Survived"][df["Sex"] == "female"].value_counts()[0]
        print(f"Number of male passengers who survived: {male_survived}")
        print(f"Number of female passengers who survived: {female_survived}")
        print(f"Number of male passengers who didn't survived: {male_notsurvived}")
        print(f"Number of female passengers who didn't survived: {female_notsurvived}")
    elif (choice == 2) and (choice2 == 4):
        df["Age"] = df["Age"].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        df['AgeGroup'] = pd.cut(df["Age"], bins, labels=labels)
        print(df['AgeGroup'].value_counts())
    elif (choice == 2) and (choice2 == 5):
        class1 = df["Survived"][df["Pclass"] == 1].value_counts()[1]
        print(f"Number of first class passengers who survived: {class1}")
        class2 = df["Survived"][df["Pclass"] == 2].value_counts()[1]
        print(f"Number of second class passengers who survived: {class1}")
        class3 = df["Survived"][df["Pclass"] == 3].value_counts()[1]
        print(f"Number of third class passengers who survived: {class3}")
    else:
        print("Invalid input. Try again later.")
        should_continue = False

    if_continue = input("Do you want to go again? Type Y for yes of N for no. \n").upper()
    if if_continue == "Y":
        should_continue = True
    else:
        print("Thank you! See you later!")
        should_continue = False
