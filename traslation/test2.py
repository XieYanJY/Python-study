import requests
import json

word = input('请输入:')
data = {
        'i': word,
        'from': 'AUTO',
        'to':' AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '16061061122206',
        'sign': 'a6f391b5a4a84296714d298f77a75977',
        'lts': '1606106112220',
        'bv': '33bafbf137bd0b36cd4f1ffa3b0dd45b',
        'doctype': 'json',
        'version': 2.1,
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }

def get_page(url):
    r = requests.get(url, params=data)
    exit if not r.status_code == requests.codes.ok else print('Request Successfully')
    # print(type(r))
    msg = r.json()
    # print(type(msg))
    # print(msg)
    print(msg['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    get_page(url)

