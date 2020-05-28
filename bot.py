from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium import webdriver
from random import randint
import socks
import socket
import time
import random
import csv

def read_csv():
    link = []
    name = []

    with open('old/buisnes.csv', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=',')
        for i, row in enumerate(reader):
            if i > 0:
                name.append(row['name'])
                link.append(row['link'])
        return name, link

def main():

    account = ['salek.don@hotmail.ru']
    answer = ['Ссылка битая', 'Пожалуйста обновите ссылку', 'Материал недоступен', 'Не могу скачать данный материал', 'не открывает ссылку', 'не работает скачка', 'не получается скачать']
    name, link = read_csv()
    i = 0
    j = 0

    while i < 150:
        #socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
        #socket.socket = socks.socksocket
        i += 1
        #j = str(randint(0, 276031))
        options = Options()
        #options.add_argument('--proxy-server=84.201.254.47:3128')
        options.add_argument("user-agent=" + UserAgent().chrome)
        #options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get('https://sharewood.biz/login/login')
        email = driver.find_element_by_name('login')
        password = driver.find_element_by_name('password')
        email.send_keys(random.choice(account))
        password.send_keys('12345678')
        email.submit()


        try:
            driver.get(random.choice(link))
            report_form = driver.find_element_by_name('message')
            report_form.send_keys(random.choice(answer))
            report_form.submit()
            j += 1
            print(j)
        except:
            print('Bad')
        time.sleep(randint(10, 300))
        driver.close()

if __name__=='__main__':
    main()
