import click
from scrap_site import scrap_data_from_website
import joblib
import pandas as pd


@click.command()
@click.option('--website_url', default="https://ensai.fr", help='The website to categorize.')
def predict_category(website_url):
    category = ['Arts', 'Business', 'Computers', 'Games', 'Health', 'Home', 'News',
       'Recreation', 'Reference', 'Science', 'Shopping', 'Society',
       'Sports']
    desc = scrap_data_from_website(website_url)
    loaded_model = joblib.load('model_pipeline/pipeline_nb.pkl')
    df = pd.DataFrame([desc], columns=['desc'])
    category_predicted_int = loaded_model.predict(df.desc.values)
    category_predicted = category[category_predicted_int[0]]
    print(category_predicted)

if __name__ == "__main__":
    predict_category()