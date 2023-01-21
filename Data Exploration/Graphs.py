import pandas as pd
import matplotlib.pyplot as plt

class Graphs:

    def __init__(self):
        df = pd.read_csv(
            r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")
        print(df)

    def histogramage(self):
        df = pd.read_csv(
            r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")
        df['Age'].plot(kind='hist', bins=20, color='grey')
        plt.show()

    def gendersplit(self, df):
        self.df = pd.read_csv(
            r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")
        explode = (0.05, 0.05)
        colors = ["steelblue", "pink"]
        df.Sex.value_counts().plot(kind='pie', y='Sex', autopct='%1.0f%%', colors=colors, explode=explode)
        plt.show()

