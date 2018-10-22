from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C://Profile//chromedriver_win32//chromedriver.exe")

# 实验一
# url = "http://iwebshop.spider.com/index.php?controller=site&action=products&id={}"
# file_name = "./page/myhtml_{}.html"
# for i in range(1, 3):
#     temp_url = url.format(i)
#     temp_file_name = file_name.format(i)
#     driver.get(temp_url)
#     html = driver.page_source
#     print(html)

#     with open(temp_file_name, "w+", encoding="utf-8") as f:
#         f.write(html)
#         f.close()
# print("Request over")

# 实验二
# page = "http://zblog.spider.com/page/{}/"
# count = 0
# for i in range(1, 4):
#     temp_page = page.format(i)
#     print(temp_page)
#     driver.get(temp_page)
#     main_html = driver.page_source
#     urls = re.findall(r"http://zblog.spider.com/post/.+?\.html", main_html)
#     for post_url in urls:
#         driver.get(post_url)
#         print(driver.title)
#         count = count + 1
#         print(count)

# 实验三
url = "http://zblog.spider.com/post/xuemian.html"   #注意带入当前页面的url
driver.get(url)
html = driver.page_source
all_li = BeautifulSoup(html, "lxml").find_all(attrs={"class": "post single"})
for li in all_li:
    title = li.find("h2").text.strip()
    time = li.find("h4").text.strip()
    body = li.find("p").text.strip()
    author_browser_comment = li.find("h6").text.strip()
    print("{} {} {} {}".format(title, time, body, author_browser_comment))

driver.quit();
