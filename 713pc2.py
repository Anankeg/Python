from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

# from urllib.request import urlopen
# import re
# import random


def main_spider(url):
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()
    driver.get("https://youpin.mi.com/")
    driver.find_element_by_xpath(u"(//a[contains(text(),'手机')])[2]").click()
    print(driver.find_element_by_xpath(u"(//a[contains(text(),'手机')])[2]"))
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html, features='lxml')
    list_soup = soup.find_all('div',
                              {'class': re.compile('pro-item m-tag-a (.*?)')})
    com_list = []
    for com_info in list_soup:
        name = com_info.find('p', {'class': 'pro-info'}).string.strip()
        desc = com_info.find('p', {'class': 'pro-desc'}).string.strip()
        price = com_info.find('span', {'class': 'm-num'}).string.strip()
        com_list.append([name, desc, price])
    print(com_list)
    # print(html)

    # name = soup.find_all('p', {"class": "pro-info"})
    # desc = soup.find_all('p', {"class": "pro-desc"})
    # price = soup.find_all('span', {'class': 'm-num'})
    # # price = soup.find_all('p', {"class": "pro-price"})
    # # print(name.get_text())
    # for n in name:
    #     print(n.get_text())

    # for d in desc:
    #     print(d.get_text())

    # for p in price:
    #     print(p.get_text())
    driver.close()


basic_url = 'https://youpin.mi.com/'
main_spider(basic_url)
