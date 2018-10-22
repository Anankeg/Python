import urllib
import urllib.request
import requests

# 打开Debug Log 方便调试
httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httpHandler, httpsHandler)
urllib.request.install_opener(opener)


data = {
    u'referer':
    u'http://api.xfsub.com/index.php?url=https://www.iqiyi.com/a_19rrh0a4p9.html',
    u'time':
    u'1533900868',
    u'key':
    u'3b22a91232f51305bdf32e6d50a73727',
    u'url':
    u'https://www.iqiyi.com/a_19rrh0a4p9.html',
    u'type':
    u'iqiyi'
}
# data = urllib.urlencode(data)
header = {
    # ':authority':
    # 'api.177537.com',
    # ':method':
    # 'POST',
    # ':path':
    # '/xfsub/api.php',
    # ':scheme':
    # 'https',
    # 'accept':
    # 'application/json,text/javascript,*/*;q=0.01',
    # 'accept-encoding':
    # 'gzip,deflate,br',
    # 'accept-language':
    # 'zh-CN,zh;q=0.9',
    # 'content-length':
    # '218',
    # 'content-type':
    # 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie':
    '__cfduid=d5b11445f13508eac6bf8ab74c00fd0f21533898111; PHPSESSID=imc3ljo74e88bppd8k7a76dqf4; UM_distinctid=1652373b2e03e2-07cd63f34ae0f5-9393265-100200-1652373b2e593f; CNZZDATA1219518=cnzz_eid%3D1320354742-1533893186-https%253A%252F%252Fwww.iqiyi.com%252F%26ntime%3D1533898589',
    'origin':
    'https://api.177537.com',
    'referer':
    'https://api.177537.com/xfsub/?url=https://www.iqiyi.com/a_19rrh0a4p9.html',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'x-requested-with':
    'XMLHttpRequest',
    # post要加入的:
}
req = requests.post(url='https://api.177537.com/xfsub/api.php', data=data, headers=header)
# response = urllib.request.urlopen(req)
print(req.text)
