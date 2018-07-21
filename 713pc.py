from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# from urllib.request import urlopen
import re
import csv
# import random


def get_urls(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    html = driver.page_source
    # print(html)
    soup = BeautifulSoup(html)
    urls_soup = soup.find_all('a', {'data-src': re.compile("^/goodsbycategory?")})
    urls = []
    for l in urls_soup:
        urls.append([l.string, l.attrs['data-src']])
    # print(urls)
    driver.close()
    return urls


def main_spider(url_info):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url_info)
    html = driver.page_source
    # print(html)
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
    driver.close()
    return list_good


def do_csv(list_good):
    with open('data2.csv', 'a',  encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        fieldnames = ['name', 'desc', 'price']
        writer.writerow(fieldnames)
        for good in list_good:
            writer.writerow(good)


basic_url = 'https://youpin.mi.com'
urls = get_urls(basic_url)
urls.pop(10)
# url_info = basic_url + str(urls[1])
# main_spider(url_info)
for l in urls:
    url_info = basic_url+l[1]
    list_good = main_spider(url_info)
    if list_good != None and len(list_good) >= 1:
        print(l[0] + '爬取成功')
    else:
        print(l[0] + 'failed')
    do_csv(list_good)
    # print(list_good)
    print('写入完成')
