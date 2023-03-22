# Gives the rank of the website given in input
import pandas as pd

df_imatag = pd.read_csv('data/imatag.csv', sep = "\t")

print(len(df_imatag))