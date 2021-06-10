import requests
import re

def get_pages(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    html = requests.get(url,headers)
    result = html.text
    return result

def get_ip(result):
    p = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
    ip = re.findall(p,result)
    # for each in ip:
    #     print(ip)
    print(ip)

if __name__ == '__main__':
    url = 'https://ip.ihuan.me/'
    get_ip(get_pages(url))