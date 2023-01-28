import pandas as pd
import matplotlib.pyplot as plt
from Graphs import Graphs
from Statistics import Statistics
df = pd.read_csv(r"https://github.com/OlaSolka/Titanic-analysis/blob/c2a442ebab23aecd292f4e3985da63a51efbafb2/train.csv")

# sex_pie = Graphs()
# print(sex_pie.gendersplit(df))

gender_numbers = Statistics()
gender_numbers.gendersplit()
#
# nodata = Statistics()
# print(nodata.isnull(df))