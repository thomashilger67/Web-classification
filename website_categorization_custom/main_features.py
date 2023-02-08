from categorization.scraping import *
import pandas as pd
import concurrent.futures

df = pd.read_csv("/home/ensai/imatag/website_categorization_custom/categorization/Datasets/Feature_dataset_2023-01-10.csv")

#df = df.sample(500)
# sample = df.sample(50)
# list_url = list(sample['url'])
list_url = list(df['url'])


def add_tokens(url):
    result = all(url)
    if len(result) == 0:
        result = []
    return result

final_token = []

with concurrent.futures.ThreadPoolExecutor(32) as executor:
    futures = []
    for url in list_url:
        futures.append(executor.submit(add_tokens, url=url))
    # for future in concurrent.futures.as_completed(futures):
    #     final_token.append(future.result())

        

for future in futures:
    try:
        final_token.append(future.result())
    except Exception as e:
        print(e)

# sample['tokens'] = final_token
# sample = sample[sample['tokens'].map(lambda d: len(d)) > 0]
df['tokens'] = final_token
df = df[df['tokens'].map(lambda d: len(d)) > 0]
df.to_csv("/home/ensai/imatag/website_categorization_custom/categorization/Datasets/Feature_dataset_2023-02-01_clean_full.csv")