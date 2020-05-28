import requests
import csv
import re
from bs4 import BeautifulSoup

from multiprocessing import Pool
from contextlib import closing



def get_html(url):
    url_auth = 'https://sharewood.biz/login/login' #ne loginitsya, tochno vse pravilno?

    login = 'what-and-where@yandex.ru'                #//////////VVEDI SUDA LOGIN/////////
    password = 'Splitispliti78317831'

    payload = {
        'login': login,
        'password': password,
        'remember': 1,
        '_xfRedirect': 'https: // sharewood.biz /',
        '_xfToken': '1566908705, a56c7264ecc08da56bff9d85b3aedb23',

    }
    with requests.Session() as s:
        p = s.post(url_auth, data=payload)
        r = s.get(url)
    return r.text


def get_all_data(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('h1', class_='p-title-value').text.strip()
    except:
        name = ''
    try:
        desc = soup.find('div', class_='bbWrapper').text.strip()
        #desc = desc.split('Скачать:')
        #desc = re.findall(r'(https?://[^\s]+)', str(desc[-1]))
    except:
        desc = ''
    try:
        link = soup.find('div', class_='bbWrapper').text.strip()
        link = link.split('Скрытый контент, для просмотра которого нужно лайкнуть пост.')
        link = re.findall(r'(https?://[^\s]+)', str(link[-1]))
        print(link)
    except:
        link = ''

    data = {'name': name,
            'desc': desc,
            'link': link}

    return data

def write_csv(data):
    with open('raznoe-link.csv', 'a') as f:
        writer = csv.writer(f, delimiter=',')

        writer.writerow((data['name'],
                         data['desc'],
                         data['link']))
        print(data['name'][0:10], 'parsed')

def read_csv():
    link = []
    name = []

    with open('raznoe.csv') as data:
        reader = csv.DictReader(data, delimiter=',')
        for i, row in enumerate(reader):
            if i > 0:
                name.append(row['name'])
                link.append(row['link'])
        return name, link

def make_data(url):
    if url != '':
        html = get_html(url)
        data = get_all_data(html)
        write_csv(data)

def main():
    name = 'name'
    desc = 'desc'
    link = 'link'
    data = {'name': name, 'desc': desc, 'link': link}
    write_csv(data)
    name, link = read_csv()
    with closing(Pool(2)) as p:
        p.map(make_data, link)
        p.terminate()


if __name__ == '__main__':
    main()
