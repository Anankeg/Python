import requests
import hashlib


url = "http://zblog.spider.com/zb_system/cmd.php?act=verify"
data = "btnPost=%E7%99%BB%E5%BD%95&username=admin&password={}&savedate=1"
header = {"Content-Type": "application/x-www-form-urlencoded"}
password = hashlib.md5(str(19960115).encode()).hexdigest()
# print(i)
print(password)
temp_data = data.format(password)
print(temp_data)
r = requests.post(url, data=temp_data, headers=header)
html = r.text
print(html)
