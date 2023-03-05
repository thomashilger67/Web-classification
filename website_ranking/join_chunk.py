import pandas as pd

df_imatag = pd.read_csv('data/imatag.csv', sep = "\t")
df_imatag = df_imatag.rename(columns={"query.source": "host"})
imatag_len = len(df_imatag)

df_final = None
chunksize = 10**6
rank_len = 0
matched_len = 0
for chunk in pd.read_csv('data/rank.csv',  sep = "\t", chunksize=chunksize):
    chunk = chunk.rename(columns={"#host_rev": "host"})
    rank_len += len(chunk)
    df_join = chunk.merge(df_imatag, on='host')
    matched_len += len(df_join)
    if df_final is None :
        df_final = df_join
    else :
        df_final = pd.concat([df_final, df_join])
    print("Current rank len : {}".format(rank_len))
    print("Current matched len : {}".format(matched_len))
    print("Current % : {}".format(matched_len/imatag_len))

df_final.to_csv("data/join.csv")