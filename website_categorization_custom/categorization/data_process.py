import pandas as pd
import ast


df = pd.read_csv("/home/ensai/imatag/website_categorization_custom/categorization/Datasets/Feature_dataset_2023-02-01_clean_full.csv")
df = df.drop("Unnamed: 0", axis = 1)

def convert_to_list(row):
    return ast.literal_eval(row['tokens'])

data = []
for index,row in df.iterrows():
    data.append({"class":row["Category"], "sentence":row["text"]})

words = []
classes = []
documents = []

for pattern in data:
    w = pattern['tokens']
    words.extend(w)
    documents.append((w, pattern['class']))
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

