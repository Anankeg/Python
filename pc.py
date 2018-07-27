from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://youpin.mi.com/goodsbycategory?firstId=88&secondId=88&title=%E5%AE%B6%E5%B1%85%E5%AE%B6%E7%BA%BA").read().decode('utf-8')
print(html)
#res = re.findall(r"<title>(.+?)</title>", html, flags=re.DOTALL)
soup = BeautifulSoup(html)
print(soup.title)
all_href = soup.find_all('script')
#print(all_href)
for l in all_href:
    print(l['src'])