# -*- coding: UTF-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
# import pandas as pd
import csv
# import unicodecsv


def do_spider(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source  # get html
    soup = BeautifulSoup(html, features='lxml')
    # print(soup.find_all('div', {'class': 'pro-item m-tag-a '}))
    # print(soup.find_all('p'))
    list_soup_1 = soup.find_all('div', {'class': 'pro-item m-tag-a '})
    list_soup_2 = soup.find_all('div', {'class': 'pro-item m-tag-a first'})
    list_soup = list_soup_1 + list_soup_2
    com_list = []
    for com_info in list_soup:
        com_title = com_info.find('p', {'class': 'pro-info'}).string.strip()
        com_desc = com_info.find('p', {'class': 'pro-desc'}).string.strip()
        com_price = com_info.find('span', {'class': 'm-num'}).string.strip()
        com_list.append([com_title, com_desc, com_price])
    # print(com_list)
    driver.close()
    return com_list


def print_lists_csv(com_lists):
    # for i in range(len(com_lists)):

    #     dataframe = pd.DataFrame({
    #         '名称': com_lists[i][0],
    #         '简介': com_lists[i][1],
    #         '价格': com_lists[i][2]
    #     })
    # dataframe.to_csv("test.csv", index=False, sep=',')
    with open('test.csv', 'a+', encoding='GB18030', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'info', 'price'])
        writer.writerows(com_lists)
        # w = unicodecsv.writer(csvfile, encoding='utf-8-sig')
        # w.writerows(com_lists)


if __name__ == '__main__':
    urls = [
        [
            '家居家纺',
            "https://youpin.mi.com/goodsbycategory?firstId=88&secondId=88&title=%E5%AE%B6%E5%B1%85%E5%AE%B6%E7%BA%BA"
        ],
        [
            '有品推荐',
            "https://youpin.mi.com/goodsbycategory?firstId=446&secondId=446&title=%E6%9C%89%E5%93%81%E6%8E%A8%E8%8D%90"
        ],
        [
            '日杂文创',
            "https://youpin.mi.com/goodsbycategory?firstId=91&secondId=91&title=%E6%97%A5%E6%9D%82%E6%96%87%E5%88%9B"
        ],
        [
            '家用电器',
            "https://youpin.mi.com/goodsbycategory?firstId=115&secondId=115&title=%E5%AE%B6%E7%94%A8%E7%94%B5%E5%99%A8"
        ],
        [
            '电视影音',
            "https://youpin.mi.com/goodsbycategory?firstId=90&secondId=90&title=%E7%94%B5%E8%A7%86%E5%BD%B1%E9%9F%B3"
        ],
        [
            '智能酷玩',
            "https://youpin.mi.com/goodsbycategory?firstId=116&secondId=116&title=%E6%99%BA%E8%83%BD%E9%85%B7%E7%8E%A9"
        ],
        [
            '笔记本',
            "https://youpin.mi.com/goodsbycategory?firstId=579&secondId=579&title=%E7%AC%94%E8%AE%B0%E6%9C%AC"
        ],
        [
            '手机',
            "https://youpin.mi.com/goodsbycategory?firstId=288&secondId=288&title=%E6%89%8B%E6%9C%BA"
        ],
        [
            '数码配件',
            "https://youpin.mi.com/goodsbycategory?firstId=89&secondId=89&title=%E6%95%B0%E7%A0%81%E9%85%8D%E4%BB%B6"
        ],
        [
            '服装配饰',
            "https://youpin.mi.com/goodsbycategory?firstId=93&secondId=93&title=%E6%9C%8D%E8%A3%85%E9%85%8D%E9%A5%B0"
        ],
        #  [
        #     '鞋靴箱包',
        #     "https://youpin.mi.com/goodsbycategory?firstId=335&secondId=335&title=%E9%9E%8B%E9%9D%B4%E7%AE%B1%E5%8C%85"
        # ],
        [
            '餐具厨房',
            "https://youpin.mi.com/goodsbycategory?firstId=140&secondId=140&title=%E9%A4%90%E5%85%B7%E5%8E%A8%E6%88%BF"
        ],
        [
            '饮食酒水',
            "https://youpin.mi.com/goodsbycategory?firstId=310&secondId=310&title=%E9%A5%AE%E9%A3%9F%E9%85%92%E6%B0%B4"
        ],
        [
            '运动健康',
            "https://youpin.mi.com/goodsbycategory?firstId=389&secondId=389&title=%E8%BF%90%E5%8A%A8%E5%81%A5%E5%BA%B7"
        ],
        [
            '出行户外',
            "https://youpin.mi.com/goodsbycategory?firstId=114&secondId=114&title=%E5%87%BA%E8%A1%8C%E6%88%B7%E5%A4%96"
        ],
        [
            '洗护美妆',
            "https://youpin.mi.com/goodsbycategory?firstId=341&secondId=341&title=%E6%B4%97%E6%8A%A4%E7%BE%8E%E5%A6%86"
        ],
        [
            '母婴亲子',
            "https://youpin.mi.com/goodsbycategory?firstId=155&secondId=155&title=%E6%AF%8D%E5%A9%B4%E4%BA%B2%E5%AD%90"
        ]
    ]
    for url in urls:
        com_lists = do_spider(url[1])
        if com_lists != None and len(com_lists) >= 1:
            print(url[0] + '爬取成功！')
        print_lists_csv(com_lists)
