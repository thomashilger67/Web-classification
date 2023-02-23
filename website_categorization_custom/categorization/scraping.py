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
    meta_list = []
    try:
        response = requests.get(url, headers=REQUEST_HEADERS, timeout=1)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')
            html_text = (soup.get_text()).replace("\n", " ")
            metas = soup.find_all('meta')
            meta_list = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
            print(url)        #to extract html code from page
    except Exception as e:
        print(f"{url} : Error")
    
    return html_text, meta_list

def transform_text(html_text : str, meta_list :list):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    cleaned_text = re.sub('[^a-zA-Z]+', ' ', str(html_text)).strip()
    tokens = word_tokenize(cleaned_text)
    tokens_lemmatize = [w for w in tokens if not w.lower() in stop_words]
    tokens_stemmed = [ps.stem(w.lower()) for w in tokens_lemmatize]
    return tokens_stemmed, meta_list

def all(url : str):
    html_text, meta_list = get_html_text(url)
    return transform_text(html_text=html_text, meta_list=meta_list)