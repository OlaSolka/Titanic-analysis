import pandas as pd


class Statistics:
    def __init__(self):
        df = pd.read_csv(
            r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")
        print(df)

    def gendersplit(self):
        df = pd.read_csv(
            r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")
        return df.Sex.value_counts()

    def isnull(self):
        df = pd.read_csv(
            r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")
        return df.isnull().sum()


