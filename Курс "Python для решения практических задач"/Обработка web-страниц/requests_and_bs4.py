import re
from collections import Counter
from bs4 import BeautifulSoup
import requests

"""
Полезные ссылки:
1) https://www.dataquest.io/blog/web-scraping-tutorial-python/
2) https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""


def func_1():
    """
    Проверяет какой язык упоминается чаще.
    """
    url = 'https://stepik.org/media/attachments/lesson/209717/1.html'
    html = requests.get(url).text
    print('Python' if html.count('Python') > html.count('C++') else 'C++')


def func_2():
    """
    Находит те строки, которые встречаются чаще всего,
    и выводит их в алфавитном порядке.
    """
    url = 'https://stepik.org/media/attachments/lesson/209719/2.html'
    html = requests.get(url).text
    regex = r'<code>(.*?)</code>'
    info = Counter(re.findall(regex, html))
    max_entry = info.most_common(1)[0][1]
    res = sorted([el for el, v in info.items() if v == max_entry])
    print(*res)


def func_3():
    """
    Находит все ссылки на странице.
    """
    url = 'https://ru.wikipedia.org/wiki/Python'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a', href=True):
        print(a['href'])


def func_4():
    """
    В каждом файле находится таблица,
    необходимо найти сумму всех чисел.
    """
    url = 'https://stepik.org/media/attachments/lesson/209723/3.html'
    # url = 'https://stepik.org/media/attachments/lesson/209723/4.html'
    # url = 'https://stepik.org/media/attachments/lesson/209723/5.html'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    print(sum([int(el.get_text()) for el in soup.find_all('td')]))


if __name__ == '__main__':
    func_4()
