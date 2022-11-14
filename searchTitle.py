import sys

import requests

from bs4 import BeautifulSoup

url = 'https://www.bbiquge.net/book/{0}'


header2 = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

if __name__ == '__main__':
    bookid = sys.argv[0]
    bookname = sys.argv[1]
    print(bookid, bookname)
    Url = url.format(12)
    res = requests.get(url=Url, headers=header2, timeout=10)
    soup = BeautifulSoup(res.text, features='html.parser')
    for i in soup.find('div', class_='zjbox').find_all('a', class_=''):
        print(i.get_text(), i['href'])

    print('--')