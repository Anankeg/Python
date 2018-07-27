from urllib.request import urlopen
import re
html = urlopen("https://youpin.mi.com/").read().decode('utf-8')
res = re.findall(r"<title>(.+?)</title>", html, flags=re.DOTALL)
print(html)