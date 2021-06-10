import requests
import json

word = '天气'

data = {
    'ie': 'utf-8',
    'f': 8,
    'rsv_bp': 1,
    'rsv_idx': 1,
    'tn': 'baidu',
    'wd': word,
    'fenlei': 256,
    'rsv_pq': 'f66e71d6002e8b1d',
    'rsv_t': 'b4fcisbFILEXgT8cLEucyNl42J3wIukXd8nzSdRuamlk7GDFm7LgBlCssDU',
    'rqlang': 'cn',
    'rsv_enter': 1,
    'rsv_dl': 'tb',
    'rsv_sug3': 8,
    'rsv_sug1': 7,
    'rsv_sug7': 101,
    'rsv_sug2': 0,
    'rsv_btype': 'i',
    'prefixsug': '%E5%94%A7%E5%94%A7%E6%AD%AA%E6%AD%AA',
    'rsp': 5,
    'inputT': 1794,
    'rsv_sug4': 2540
}

r = requests.get('https://www.baidu.com/', params=data)
print(r.status_code)
# print(r.cookies)
# print(type(r))
print(r.text)