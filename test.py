from bs4 import BeautifulSoup
import requests
import csv
import re

def main():
    with open("161.txt", encoding='utf-8') as file:
        url = file.read()

    soup = BeautifulSoup(url, 'lxml')
    try:
        author = soup.find('div', class_='bbWrapper').text.strip()
        author = author.split('Автор:')
        author = author[1].split('\n')
        author = author[0].strip()
        print(author)
    except:
        author = ''

    try:
        name = soup.find('div', class_='bbWrapper').text.strip()
        name = name.split('Название:')
        name = name[1].split('\n')
        name = name[0].strip()
        print(name)
    except:
        name = ''

    # try:
    #     desc = soup.find('div', class_='bbWrapper').text.strip()
    #     desc = desc.split('Описание:')
    #     desc = desc[1].split('Подробнее:')
    #     desc = desc[0].strip()
    #     print(desc)
    # except:
    #     desc = ''
    #
    # try:
    #     detail = soup.find('div', class_='bbWrapper').text.strip()
    #     detail = detail.split('Подробнее:')
    #     detail = detail[1].split('Скачать:')
    #     detail = detail[0].split('Скрытый контент для авторизованных пользователей.')
    #     detail = detail[1].strip()
    #     print(detail)
    # except:
    #     detail = ''
    #
    # try:
    #     dwnld = soup.find('div', class_='bbWrapper').text.strip()
    #     dwnld = dwnld.split('Скачать:')
    #     dwnld = dwnld[1].split('Скрытый контент, для просмотра которого нужно лайкнуть пост.')
    #     dwnld = dwnld[1].strip()
    #     print(dwnld)
    # except:
    #     dwnld = ''

if __name__ == '__main__':
    main()