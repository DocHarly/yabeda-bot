from selenium import webdriver
from random import randint
import time
import random
import csv

def read_csv():
    link = []
    name = []

    with open('buisnes-link.csv', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=',')
        for i, row in enumerate(reader):
            if i > 0:
                name.append(row['name'])
                link.append(row['link'])
        return name, link

def main():

    account = ['lorik@yandex.ru', 'tathi@mail.ru', 'rurik@gmail.com', 'kaspar@bk.ru', 'dm@yandex.ru', 'sosiska@mail.ru', 'razrik@gmail.com', 'bruk-for-rizen-de-vol@yandex.ru', 'pis@mail.ru', 'vekna@gmail.com']
    answer = ['Ссылка битая', 'Пожалуйста обновите ссылку', 'Материал недоступен', 'Не могу скачать данный материал', 'не открывает ссылку', 'не работает скачка']
    name, link = read_csv()
    i = 0
    j = 0

    while i < 150:
        i += 1
        #j = str(randint(0, 276031))
        driver = webdriver.Chrome()
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
        time.sleep(randint(2, 10))
        driver.close()

if __name__=='__main__':
    main()
