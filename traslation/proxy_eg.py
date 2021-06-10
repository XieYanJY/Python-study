# 添加代理
'''
1.参数是一个字典{'类型'：'代理ip：端口号'}
proxy_support = urllib.request.ProxyHandler({})
2.定制、创建一个opener
opener = urllib.request.build_opener(proxy_support)
3.安装opener
urllib.request.install_opener(opener)
4.调用opener
opener.open()
'''

import urllib.request
import random
# import urllib.parse

ip = ['119.81.189.194:8123','153.36.134.200:9999','113.254.90.12:80']


# proxy_support = urllib.request.ProxyHandler({'https':random.choice(ip)})
proxy_support = urllib.request.ProxyHandler({'https':'138.117.85.153:999'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15')]

# urllib.request.install_opener(opener)



url = 'https://www.baidu.com'


response = opener.open(url)
html = response.read().decode('utf-8')
print(html)

