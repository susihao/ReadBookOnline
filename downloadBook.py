import os
import requests
from lxml import etree
import time
import random
import sys

baocunPath = r'D:/pyand/'
headers = {
    "Referer": "http://www.xbiquge.la/0/951/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1"
}


def get_urls():
    url = 'http://www.xbiquge.la/0/951/'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = etree.HTML(res.text)
    url_list = ['http://www.xbiquge.la' + x for x in html.xpath('//div[@id="list"]/dl/dd/a/@href')]
    return url_list


def get_text(url):
    rep = requests.get(url, headers=headers)
    rep.encoding = 'utf-8'
    dom = etree.HTML(rep.text)

    SuBooks = 'nihao'
    nowBook = 'nnnnn'

    name = dom.xpath('//div[@class="bookname"]/h1/text()')[0]
    text = dom.xpath('//div[@id="content"]/text()')
    if os.path.exists(f'{SuBooks}'):
        if os.path.exists(f'{SuBooks}/{nowBook}'):
            baocunPathB = baocunPath+f'{SuBooks}/{nowBook}/'
        else:
            os.mkdirs(f'{SuBooks}/{nowBook}')
            baocunPathB = baocunPath + f'{SuBooks}/{nowBook}/'
    else:
        os.makedirs(f'{SuBooks}/{nowBook}')
        baocunPathB = baocunPath + f'{SuBooks}/{nowBook}/'

    with open(baocunPathB + f'{name}.txt', 'w', encoding='utf-8') as f:
        for con in text:
            f.write(con)
    print(f'{name} 下载完成！')


def main():
    urls = get_urls()
    for url in urls:
        get_text(url)
        time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    main()
