import pandas as pd

df_rank = pd.read_csv('data/rank.csv',  sep = "\t")
df_rank = df_rank.rename(columns={"#host_rev": "host"})
df_imatag = pd.read_csv('data/imatag.csv', sep = "\t")
df_imatag = df_imatag.rename(columns={"query.source": "host"})

print("df_rank : {}".format(len(df_rank)))
print("df_imatag : {}".format(len(df_imatag)))

df_join = df_rank.merge(df_imatag, on='host')

print("df_join : {}".format(len(df_join)))
print("df_join/df_imatag : {}".format(len(df_join)/len(df_imatag)))