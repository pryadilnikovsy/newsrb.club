import requests
import codecs
from bs4 import BeautifulSoup as bs

def work(url):
    url = 'https://zhilstroynadzor.bashkortostan.ru/presscenter/news/'
    url_image = 'https://zhilstroynadzor.bashkortostan.ru'
    resp = requests.get(url)
    news = []
    errors = []
    if resp.status_code == 200:
        soup = bs(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'news'})
        if main_div:
            div_lsts = main_div.findAll('div', attrs={'class': 'news__item'})
            for lst in div_lsts:
                title = lst.find('a', attrs={'class': 'news__title-link'})
                href = url + title['href']
                news_preview = lst.find('div', attrs={'class': 'news__preview'}).text
                news_image = lst.find('img', attrs={'class': 'news__photo'})
                src_image = url_image + news_image['src']
                news.append({'title_text': title.text, 'href': href, 'news_preview': news_preview, 'news_image': src_image})

        else:
            errors.append({'href': url, 'title': 'Div not found'})
    else:
        errors.append({'href': url, 'title': 'Page do not response'})