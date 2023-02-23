from categorization.scraping import *
import pandas as pd
import concurrent.futures

df = pd.read_csv("/home/ensai/imatag/website_categorization_custom/categorization/Datasets/Feature_dataset_2023-01-10.csv")

#df = df.sample(500)
# sample = df.sample(50)
# list_url = list(sample['url'])
list_url = list(df['url'])


def add_tokens(url):
    result_tokens, metades = all(url)
    if len(result_tokens) == 0:
        result_tokens = []
    if len(metades) == 0:
        metades = []
    return result_tokens, metades

final_token = []
final_meta = []
with concurrent.futures.ThreadPoolExecutor(32) as executor:
    futures = []
    for url in list_url:
        futures.append(executor.submit(add_tokens, url=url))
    # for future in concurrent.futures.as_completed(futures):
    #     final_token.append(future.result())

        

for future in futures:
    try:
        tok, des = future.result()
        final_token.append(tok)
        final_meta.append(des)
    except Exception as e:
        print(e)

# sample['tokens'] = final_token
# sample = sample[sample['tokens'].map(lambda d: len(d)) > 0]
df['tokens'] = final_token
df['metadescription'] = final_meta
df = df[df['tokens'].map(lambda d: len(d)) > 0]
df = df[df['metadescription'].map(lambda d: len(d)) > 0]
df = df[df['metadescription'].map(lambda d: d[0]) != '']
df.to_csv("/home/ensai/imatag/website_categorization_custom/categorization/Datasets/Feature_dataset_2023-02-08_clean_full_meta.csv")