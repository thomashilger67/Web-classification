import click
from scrap_site import scrap_data_from_website
import joblib

test1 = "https://help.twitter.com"
test2 = "https://ensai.fr"

@click.command()
@click.option('--website_url', default="https://ensai.fr", help='The website to categorize.')
def predict_category(website_url):
    tokens = scrap_data_from_website(website_url)
    loaded_model = joblib.load('my_model_knn.pkl.pkl')
    caegory_predicted = loaded_model.predict(tokens)

if __name__ == "__main__":
    predict_category()