import requests
import execjs
from pprint import pprint
headers = {
    "authority": "api.qimai.cn",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://www.qimai.cn",
    "pragma": "no-cache",
    "referer": "https://www.qimai.cn/",
    "sec-ch-ua": "^\\^Chromium^^;v=^\\^110^^, ^\\^Not",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
cookies = {
    "Hm_lvt_ff3eefaf44c797b33945945d0de0e370": "1677052414",
    "PHPSESSID": "khic8mf744kf64eo1vpfikuhvu",
    "qm_check": "A1sdRUIQChtxen8tJ0NMMRcOUFseEHBeQF0NSjFNWDE+FXBAUUlYXVsSQldUSElacV5AVVpEB3xQU0MSCyZPagcSQEpvAWdRTkMgSz1LBB4QHBtTXF0CCUFeWklWBRsCHAkcBBoc",
    "gr_user_id": "cd2cd125-258c-4691-8d66-e5b1ec240613",
    "ada35577182650f1_gr_session_id": "3bde4003-4859-4b00-b65e-38e27f4f069f",
    "ada35577182650f1_gr_session_id_3bde4003-4859-4b00-b65e-38e27f4f069f": "true",
    "synct": "1677292528.117",
    "Hm_lpvt_ff3eefaf44c797b33945945d0de0e370": "1677292530",
    "syncd": "-889869"
}
url = "https://api.qimai.cn/rank/index"
cell = execjs.compile(open('quimai.js', encoding='utf-8').read())


params = {
    "brand": "free",
    "device": "iphone",
    "country": "cn",
    "genre": "36",
    "date": "2023-02-25",
    "page": "3",
    "is_rank_index": "1"
}
keu = list(params.values())
print(keu)
analysis = cell.call('_xl', keu, '/rank/index')
params['analysis'] = analysis
response = requests.get(url, headers=headers, cookies=cookies, params=params)
# pprint(response.json())
pprint(response.json().get('rankInfo'))
# 50 lines of data per page