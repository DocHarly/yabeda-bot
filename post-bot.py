from selenium import webdriver
from random import randint
import time
import csv
import re

def read_csv():
    desc = []
    detail = []
    name = []
    author = []
    dwnld = []

    with open('sport-link.csv', encoding='utf-8') as data:
        reader = csv.DictReader(data, delimiter=',')
        for i, row in enumerate(reader):
            if i > 1649:   # > 207
                author.append(row['author'])
                name.append(row['name'])
                desc.append(row['desc'])
                detail.append(row['detail'])
                dwnld.append(row['dwnld'])
        return author, name, desc, detail, dwnld

def main():
    author, name, desc, detail, dwnld = read_csv()
    #print(desc[1])
    mail = ['DocHarly', 'split-i-split@yandex.ru']
    pas = ['484715hp', 'Spliti7831']
    logg = randint(0, 1)

    driver = webdriver.Chrome()
    driver.get('https://www.eldoradoland.xyz/login/')
    email = driver.find_element_by_name('login')
    password = driver.find_element_by_name('password')
    email.send_keys(mail[logg])
    password.send_keys(pas[logg])
    email.submit()
    j = 0
    for i in range(len(name)):
        if (name[i]=='') | (desc[i]=='') | (dwnld[i]==''):
            continue
        try:
            driver.get('https://www.eldoradoland.xyz/form/86/select')

            ###################
            ### Автор поста ###
            ###################

            post_form = driver.find_element_by_name('question[657]')
            try:
                post_author = author[i].split('\n')
                if post_author[0] != '':
                    post_form.send_keys(post_author[0])
                else:
                    post_form.send_keys('Неизвестен')
            except:
                post_form.send_keys('Неизвестен')

            ######################
            ### Название поста ###
            ######################

            post_form = driver.find_element_by_name('question[658]')
            post_name = name[i].split('\n')
            print(post_name[0])
            post_form.send_keys(post_name[0])

            ##################
            ### Тело поста ###
            ##################

            post_desc = desc[i].split('Скачать:')
            post_form = driver.find_element_by_xpath(".//div[@class='fr-element fr-view']/p[1]").send_keys(post_desc[0])

            #################
            ### Подробнее ###
            #################

            post_form = driver.find_element_by_name('question[660]')
            post_form.send_keys(detail[i])

            ##############
            ### Купить ###
            ##############

            hover = driver.find_element_by_class_name('formRow-explain')
            webdriver.ActionChains(driver).move_to_element(hover).perform()
            hover = driver.find_element_by_id('xfCustom_buy-2')
            webdriver.ActionChains(driver).move_to_element(hover).perform()
            post_form = driver.find_element_by_id('xfCustom_buy-2').click()
            time.sleep(5)
            post_form = driver.find_element_by_id('editor_hide_text').send_keys(dwnld[i])
            post_form = driver.find_element_by_id('editor_hide_submit').click()
            time.sleep(2)

            ###############
            ### Скачать ###
            ###############

            hover = driver.find_element_by_name('question[661]')
            #webdriver.ActionChains(driver).move_to_element(hover).perform()
            post_form = driver.find_element_by_name('question[661]')
            post_form.send_keys(dwnld[i])

            time.sleep(3)
            post_form.submit()

        except:
            print("bad iteration " + str(i))
            continue

if __name__=='__main__':
    main()