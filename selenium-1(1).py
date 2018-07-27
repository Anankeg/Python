from selenium import webdriver
from bs4 import BeautifulSoup
# import pandas as pd
import csv


def do_spider(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source  # get html
    soup = BeautifulSoup(html)
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
    print(com_list)
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
    with open('test.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['name', 'info', 'price'])
        writer.writerows(com_lists)


if __name__ == '__main__':
    url = "https://youpin.mi.com/goodsbycategory?firstId=288&secondId=288&title=%E6%89%8B%E6%9C%BA"
    com_lists = do_spider(url)
    print_lists_csv(com_lists)
