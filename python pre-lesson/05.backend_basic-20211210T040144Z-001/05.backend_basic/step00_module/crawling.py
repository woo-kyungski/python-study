import requests
from bs4 import BeautifulSoup

def crawling_sites(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    articles = soup.find_all('div', 'article-body content-width wysiwyg-content inarticle-link-tracking fs-article')
    site_list = []
    for article in articles[1:]:
        for site in article.find_all('h2'):
            site_list.append(site.get_text())
            
    return site_list