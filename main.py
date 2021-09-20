from bs4 import BeautifulSoup as bs
import requests
import json
import re

#sochinews
url = "https://sochinews.io/feed/"
req = requests.get(url)

bs_content = bs(req.content, "xml")    # контент feed'а
items = bs_content.find_all("item")

# Разбиваем items на элементы
news_items = []

for item in items:
    news_item = {}

    news_item['название'] = item.title.text.strip()
    news_item['категория'] = item.category.text.strip()

    url = item.link.text
    if re.match('https://sochinews.io', url):
        bs_content = bs(requests.get(url).content, "lxml")
        news_item['текст новости'] = bs_content.find("div", class_='td-post-content td-pb-padding-side').text.strip()

    news_item['источник'] = 'Ежедневное новостное сетевое издание «Sochinews»'
    news_item['ссылка'] = item.link.text.strip()
    news_item['дата публикации'] = item.pubDate.text.strip()
    news_items.append(news_item)



# sochi24
url1 = "https://sochi24.tv/feed"
req1 = requests.get(url1)

bs_content1 = bs(req1.content, "xml")
items1 = bs_content1.find_all("item")

for item in items1:
    news_item1 = {}

    news_item1['название'] = item.title.text.strip()
    news_item1['категория'] = item.category.text.strip()

    url1 = item.link.text
    if re.match('https://sochi24.tv', url1):
        bs_content1 = bs(requests.get(url1).content, "lxml")
        news_item1['текст новости'] = item.encoded.text.strip()

    news_item1['источник'] = 'Сочинский городской портал Sochi24.tv'
    news_item1['ссылка'] = item.link.text.strip()
    news_item1['дата публикации'] = item.pubDate.text.strip()
    news_items.append(news_item1)




# sochiexpress
url2 = "https://sochi-express.ru/feed"
req2 = requests.get(url2)

bs_content2 = bs(req2.content, "xml")
items2 = bs_content2.find_all("item")

for item in items2:
    news_item2 = {}

    news_item2['название'] = item.title.text.strip()
    news_item2['категория'] = item.category.text.strip()

    url2 = item.link.text
    if re.match('https://sochi-express.ru/', url2):
        bs_content2 = bs(requests.get(url2).content, "lxml")
        news_item2['текст новости'] = item.encoded.text.strip()

    news_item2['источник'] = 'Городской новостной портал Сочи Экспресс'
    news_item2['ссылка'] = item.link.text.strip()
    news_item2['дата публикации'] = item.pubDate.text.strip()
    news_items.append(news_item2)




# Экспортируем в json
with open('news-test.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(news_items, indent=4, ensure_ascii=False))


