import click


test1 = "https://help.twitter.com"
test2 = "https://ensai.fr"

@click.command()
@click.option('--start_url', default="https://ensai.fr", help='The starting point of the crawler.')
@click.option('--min_websites',  default= 30,
              help='The minimum number of pages to crawl.')
def run_crawler(start_url, min_websites):
    crawler = Crawler(max_websites=min_websites)
    pages_found = crawler.run(start_url)
    utils.list_to_txt(url_list= pages_found, filename= "results/crawled_webpages.txt")


if __name__ == "__main__":
    run_crawler()