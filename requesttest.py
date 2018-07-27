import requests
import webbrowser

data = {"result": {"model": "Homepage", "action": "GetGroup2ClassInfo", "parameters": {}}}
cookies = {'youpindistinct_id': '1648ab8ceb395-08abcb1e981e45-6114167a', 'UM_distinctid': '1648ab8d1ce66c-0fe46aebb7363a-6114167a-100200-1648ab8d1d01fa', 'Hm_lvt_f60d40663f1e63b337d026672aca065b': ['1531335726', '1531383018', '1531480322'], 'youpin_sessionid': '1649369e106-07f0c6c69e5244-1ecf', 'mjclient': 'pc', 'CNZZDATA1267968936': '1422189747-1531335527-%7C1531492536', 'CNZZDATA1256793290': '1562832432-1531331947-%7C1531493948', 'Hm_lpvt_f60d40663f1e63b337d026672aca065b': '1531497040'}
r = requests.post('https://youpin.mi.com/app/shopv3/pipe', data=data, cookies=cookies)
print(r)