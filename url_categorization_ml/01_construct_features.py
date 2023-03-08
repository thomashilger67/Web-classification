import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import config
import nltk
import pickle
from functions import timeit, scrape, parse_request

import ast

def convert_to_list(row):
    return ast.literal_eval(row['tokens'])

df = pd.read_csv(config.MAIN_DATASET_PATH, names=['0', 'url', 'main_category'])
#df = df.rename(columns={'main_category:confidence': 'main_category_confidence'})
df = df.drop(['0'], axis=1)
df = df[['url', 'main_category']]

df = df[df['main_category'] != 'Adult']
df = df[df['main_category'] != 'Kids']
#print(df[:10])

df = df.groupby('main_category').apply(
    lambda x: x.sample(frac=0.01)
)
df = df.droplevel(0)
#df['url'] = df['url'].apply(lambda x: 'http://' + x)
#df['tld'] = df.url.apply(lambda x: str(x).split('.')[-1])
#df = df[df.tld.isin(config.TOP_LEVEL_DOMAIN_WHITELIST)].reset_index(drop=True)
df['tokens'] = ''
print(len(df))
print("Scraping begins. Start: ", datetime.now())
with ThreadPoolExecutor(config.THREADING_WORKERS) as executor:
    start = datetime.now()
    results = executor.map(scrape, [(i, elem) for i, elem in enumerate(df['url'])])
exec_1 = timeit(start)
print('Scraping finished. Execution time: ', exec_1)

print("Analyzing responses. Start: ", datetime.now())
with ProcessPoolExecutor(config.MULTIPROCESSING_WORKERS) as ex:
    start = datetime.now()
    res = ex.map(parse_request, [(i, elem) for i, elem in enumerate(results)])

list_tok = []

for props in res:
    i = props[0]
    tokens = props[1]
    print(tokens)
    list_tok.append(tokens)
exec_2 = timeit(start)
print('Analyzing responses. Execution time: ', exec_2)
print(len(list_tok))
print(len(df))
df['tokens'] = list_tok
df.to_csv(config.TOKENS_PATH, index=False)

""" print('Generating words frequency for each category: ', datetime.now())
start = datetime.now()
words_frequency = {}
for category in df.main_category.unique():
    print(category)
    all_words = []
    df_temp = df[df.main_category == category]
    for word in df_temp.tokens:
        all_words.extend(word)
    most_common = [word[0] for word in nltk.FreqDist(all_words).most_common(config.FREQUENCY_TOP_WORDS)]
    words_frequency[category] = most_common

# Save words_frequency model
pickle_out = open(config.WORDS_FREQUENCY_PATH, "wb")
pickle.dump(words_frequency, pickle_out)
pickle_out.close()

exec_3 = timeit(start)
print('Generating words frequency for each category Finished. Execution time: ', exec_3)

print('Script finished.\nTimes log:\nPart 1: ', exec_1, '\nPart 2: ', exec_2, '\nPart 3: ', exec_3)
 """