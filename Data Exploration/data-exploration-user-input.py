import pandas as pd
import warnings
from art import logo
from choices import Choices
warnings.filterwarnings('ignore')

print(logo)

print("Hi, welcome to the titanic catastrophe data exploration!")

should_continue = True
df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\train.csv")
choice2 = Choices(df)
choice3 = Choices(df)

while should_continue:
    df = pd.read_csv(r"C:\Users\solka\PycharmProjects\Titanic-Analysis\train.csv")
    choice = int(input("What do you want to generate? Type '1' for graph or '2' for numbers\n"))
    if choice == 1:
        choice2.choice2()
    elif choice == 2:
        choice3.choice3()
    else:
        print("Invalid input. Try again later.")
        should_continue = False

    if_continue = input("Do you want to go again? Type Y for yes of N for no. \n").upper()
    if if_continue == "Y":
        should_continue = True
    else:
        print("Thank you! See you later!")
        should_continue = False
