from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import csv
import re

def read_csv():
    desc = []
    link = []
    name = []

    with open('buisnes-link2.csv', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=',')
        for i, row in enumerate(reader):
            if i > 0:
                name.append(row['name'])
                desc.append(row['desc'])
                link.append(row['link'])
        return name, desc, link

def main():
    name, desc, link = read_csv()
    #print(desc[1])

    # driver = webdriver.Chrome()
    # driver.get('https://www.eldorado-land.ru/login/')
    # email = driver.find_element_by_name('login')
    # password = driver.find_element_by_name('password')
    # email.send_keys('DocHarly')
    # password.send_keys('484715hp')
    # email.submit()

    for i in range(len(name)):
        if not name[i].strip():
            continue
        try:
            #driver.get('https://www.eldorado-land.ru/form/2/select')

            ###################
            ### Автор поста ###
            ###################

            # post_form = driver.find_element_by_name('question[30]')
            # try:
            #     post_author = name[i].split('[', maxsplit=1)
            #     post_author = post_author[1].split(']', maxsplit=1)
            #     print(post_author[0])
            #     post_form.send_keys(post_author[0])
            # except:
            #     post_form.send_keys('Неизвестен')
            #
            # ######################
            # ### Название поста ###
            # ######################
            #
            # post_form = driver.find_element_by_name('question[32]')
            # post_name = name[i].split(']', maxsplit=1)
            # post_form.send_keys(post_name[1])


            #post_desc = re.split(r'Название:', desc[i])
            #post_desc = re.split(r'(Подробнее:)|(Скачать:)', post_desc[-1])
            #post_form = driver.find_element_by_xpath(".//div[@class='fr-element fr-view']/p[1]").send_keys(post_desc[0])



        except:
            print("bad iteration " + str(i))
            continue

if __name__=='__main__':
    main()