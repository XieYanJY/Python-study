
import urllib.parse
import urllib.request
import json,time

def get_page(url,word):
    date = {
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
    '''使用urlencode（）编码成URL格式'''
    date = urllib.parse.urlencode(date).encode('utf-8')
    response = urllib.request.urlopen(url,date)
    html = response.read().decode('utf-8')
    return html

def parse_html(html):
    msg = json.loads(html)
    result = msg['translateResult'][0][0]['tgt']
    print(result)

def main():
    u = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    parse_html(get_page(u,word))

if __name__ == '__main__':
    while True:
        word = input('输入(输入q退出)：')
        if word == 'q':
            break
        main()
        time.sleep(5)


