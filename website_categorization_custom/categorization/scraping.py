import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer



def get_html_text(url : str):
    REQUEST_HEADERS = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}
    html_text = ''
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=3)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')
            html_text = (soup.get_text()).replace("\n", " ")
            print(url)        #to extract html code from page
    except Exception as e:
        print(e)
    
    return html_text

def transform_text(html_text : str):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    cleaned_text = re.sub('[^a-zA-Z]+', ' ', str(html_text)).strip()
    tokens = word_tokenize(cleaned_text)
    tokens_lemmatize = [w for w in tokens if not w.lower() in stop_words]
    tokens_stemmed = [ps.stem(w.lower()) for w in tokens_lemmatize]
    return tokens_stemmed

def all(url : str):
    return transform_text(get_html_text(url))