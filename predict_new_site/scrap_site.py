import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

def scrap_data_from_website(url : str):
    REQUEST_HEADERS = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}
    html_text = ''
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=1)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')
            html_text = (soup.get_text()).replace("\n", " ")
    except Exception as e:
        return(f"{url} : Error")
    stop_words = set(stopwords.words('english'))
    cleaned_text = re.sub('[^a-zA-Z]+', ' ', str(html_text)).strip()
    tokens = word_tokenize(cleaned_text)
    tokens_lemmatize = [w.lower() for w in tokens if not w.lower() in stop_words]
    desc = " ".join(tokens_lemmatize)
    return desc
