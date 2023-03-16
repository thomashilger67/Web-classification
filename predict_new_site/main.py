import click
from scrap_site import scrap_data_from_website

test1 = "https://help.twitter.com"
test2 = "https://ensai.fr"

@click.command()
@click.option('--website_url', default="https://ensai.fr", help='The website to categorize.')
def predict_category(website_url):
    tokens = scrap_data_from_website(website_url)
    print(tokens[:20])

if __name__ == "__main__":
    predict_category()