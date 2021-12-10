import requests
from bs4 import BeautifulSoup

def crawling_sites(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.find_all('div', 'article-body content-width wysiwyg-content inarticle-link-tracking fs-article')
    countries_list = []
    for article in articles[1:]:
        for country in article.find_all('h2'):
            countries_list.append(country.get_text())
            
    return countries_list