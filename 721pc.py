from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# from urllib.request import urlopen
import re
import csv
# import random


def get_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    html = driver.page_source
    # print(html)
    driver.close()
    return html


def get_menu(html):
    soup = BeautifulSoup(html)
    urls_soup = soup.find_all('a', {'data-src': re.compile("^/goodsbycategory?")})
    urls = []
    for l in urls_soup:
        urls.append([l.string, l.attrs['data-src']])
    # print(urls)
    return urls


def menu_spider(html):
    soup = BeautifulSoup(html)
    # print(soup)
    list_info = soup.find_all('div', {'class': re.compile("^pro-item m-tag-a ")})
    list_good = []
    for li in list_info:
        list_title = li.find('p', {'class': 'pro-info'}).string.strip()
        list_desc = li.find('p', {'class': 'pro-desc'}).string.strip()
        pro_price = li.find('p', {'class': 'pro-price'}).stripped_strings
        mid_price = []
        # list_price = []
        for string in pro_price:
            mid_price.append(string)
        # list_price.append(" ".join(mid_price))
        list_price = " ".join(mid_price)
        list_good.append([list_title, list_desc, list_price])
        # print(list_good)
    return list_good


def good_spider(html):
    # print(html)
    soup = BeautifulSoup(html)
    list_good = []
    if soup.find('div', {'class': 'sku-container'}) != None and soup.find('div', {'class': 'summary'}) != None:
        list_title = soup.find('div', {'class': 'good-name fl'}).string.strip()
        # print(list_title)
        list_desc = soup.find('div', {'class': 'summary'}).string.strip()
        list_price = soup.find('span', {'class': 'value'}).string.strip()
        list_good.append(list_title)
        list_good.append(list_desc)
        list_good.append(list_price)
    # else:
    #     print(html)
    return list_good


def do_csv(list_goods):
    with open('data2.csv', 'a',  encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        fieldnames = ['name', 'desc', 'price']
        writer.writerow(fieldnames)
        for good in list_goods:
            writer.writerow(good)


basic_url = 'https://youpin.mi.com'
item = '/detail?gid=%s'
id = 1
list_goods = []
while id < 2826:
    url = basic_url + item % id
    html = get_html(url)
    list_good = good_spider(html)
    if list_good != []:
        list_goods.append(list_good)
    print(list_good)
    print(id)
    id = id + 1
# print(list_goods)
# do_csv(list_goods)
# urls = get_urls(basic_url)
# urls.pop(10)
# # url_info = basic_url + str(urls[1])
# # main_spider(url_info)
# for l in urls:
#     url_info = basic_url+l[1]
#     list_good = main_spider(url_info)
#     if list_good != None and len(list_good) >= 1:
#         print(l[0] + '爬取成功')
#     else:
#         print(l[0] + 'failed')
#     do_csv(list_good)
#     # print(list_good)
#     print('写入完成')
