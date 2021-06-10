import requests,re,json

#
def get_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Cookie': 'uuid_n_v=v1; uuid=4E060BF0229611EBAC4EC35EDE93035F6627E444AFBB4D48A0FD66E8E0902688; _csrf=514462ed27246258e2bbecf59e78f780258c2229bccb637c9a48ea8d8b27c464; _lxsdk_cuid=175ad5e9debc8-07972dbcf9781b-32657007-13c680-175ad5e9debc8; _lxsdk=4E060BF0229611EBAC4EC35EDE93035F6627E444AFBB4D48A0FD66E8E0902688; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1604931469,1604931589; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1604932343; __mta=214720168.1604931473374.1604931589955.1604932664778.3; _lxsdk_s=175b7a0fba2-a24-c1-736%7C%7C1'
    }
    response = requests.get(url, headers = headers, verify = False)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    return 'nothing'



def parse_html(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?</dd>', re.S)
    result = re.findall(pattern, html)
    for i in result:
         yield {
             'index': i[0],
               'image': i[1],
               'movie': i[2],
               'actors': i[3].strip(),
               'time': i[4],
               'score': i[5]

        }
    # print(result)

# print(parse_html(main()))

def write_to_file(content):
    with open('catch_maoyan2.txt','a', ) as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_page(url)
    for i in parse_html(html):
        write_to_file(i)

if __name__ == '__main__':
    for i in range(0,100,10):
        main(offset=i)
    # time.sleep(1)



# <dd>.*?board-index.*?>(.*?)</i>.*?name.*?a.*?>(.*?)</a>.*?star.*?(.*?)</p>.*?releasetime.*?>(.*?)integer.*?>(.*?)</i>.*?</dd>
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?</dd>
# context = ssl._create_unverified_context()
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36','Cookie': 'uuid_n_v=v1; uuid=4E060BF0229611EBAC4EC35EDE93035F6627E444AFBB4D48A0FD66E8E0902688; _csrf=514462ed27246258e2bbecf59e78f780258c2229bccb637c9a48ea8d8b27c464; _lxsdk_cuid=175ad5e9debc8-07972dbcf9781b-32657007-13c680-175ad5e9debc8; _lxsdk=4E060BF0229611EBAC4EC35EDE93035F6627E444AFBB4D48A0FD66E8E0902688; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1604931469,1604931589; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1604932343; __mta=214720168.1604931473374.1604931589955.1604932664778.3; _lxsdk_s=175b7a0fba2-a24-c1-736%7C%7C1'}
# html = requests.get('https://maoyan.com/board',headers=headers, verify = False)
# # print(html.text)
# print(html.status_code)
# pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?</dd>', re.S)
# result = re.findall(pattern, html.text)
# print(result)



