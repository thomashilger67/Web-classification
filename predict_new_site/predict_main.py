import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import click
from scrap_site import scrap_data_from_website
from predict_bayesian import predict_bayesian
from predict_nn import predict_nn
from predict_bert import predict_bert
import pandas as pd


@click.command()
@click.option('--website_url', default="https://ensai.fr", help='The website to categorize.')
@click.option('--predict_proba', default=False, help='')
@click.option('--model', default=1, help='')
def predict_category(website_url,predict_proba, model):
    desc = scrap_data_from_website(website_url)
    df_data_website = pd.DataFrame([desc], columns=['desc'])
    if model == 1:
        result = predict_bayesian(df_data_website, predict_proba)
    elif model == 2:
        result = predict_nn(df_data_website, predict_proba)
    elif model == 3:
        result = predict_bert(desc, predict_proba)
    print(result)

if __name__ == "__main__":
    predict_category()