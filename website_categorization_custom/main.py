from categorization.scraping import *
import pandas as pd

def add_tokens():
    df = pd.read_csv("/home/ensai/imatag/website_categorization_custom/categorization/Datasets/Feature_dataset_2023-01-10.csv")
    df = df.sample(n = 10)
    df['tokens'] = df['url'].apply(all)
    df = df[df['tokens'].map(lambda d: len(d)) > 0]
    print(df.head(10))

add_tokens()