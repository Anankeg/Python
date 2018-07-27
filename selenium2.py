from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://youpin.mi.com/")
driver.find_element_by_link_text(u"家居家纺").click()
driver.find_element_by_link_text(u"日杂文创").click()
driver.find_element_by_link_text(u"家用电器").click()
driver.find_element_by_link_text(u"智能酷玩").click()
driver.find_element_by_link_text(u"笔记本").click()

html = driver.page_source
driver.get_screenshot_as_file("F:/python/img/screenshot2.png")
driver.close()
