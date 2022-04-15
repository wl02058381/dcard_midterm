from json import JSONDecoder, JSONEncoder
import json
import requests
from bs4 import BeautifulSoup
import json

# 爬全部文章（最新）
def news():
    rs = requests.session()
    res = rs.get(
        'https://www.dcard.tw/service/api/v2/posts?popular=false')
    # print(res.text)
    print(json.loads(res.text))
    data = json.loads(res.text)
    with open('./data/news.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 爬全部文章（熱門）
def popular():
    rs = requests.session()
    res = rs.get(
        'https://www.dcard.tw/service/api/v2/posts?popular=true')
    # print(res.text)
    print(json.loads(res.text))
    data = json.loads(res.text)
    with open('./data/popular.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 爬追星版
def entertainer():
    rs = requests.session()
    res = rs.get(
        'https://www.dcard.tw/service/api/v2/forums/entertainer/featuredPosts')
    # print(res.text)
    print(json.loads(res.text))
    data = json.loads(res.text)
    with open('./data/entertainer.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    news()
    popular()
    entertainer()
