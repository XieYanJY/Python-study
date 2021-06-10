from pyquery import PyQuery as pq
import requests

# # import chardet
#
# # with open('/Users/apple/PycharmProjects/get_movies/BeautifulSoup/university_ranking_2020.txt','rb') as f:
# #f = f.read()#.decode('utf-8').encode('utf-8')
# # print(chardet.detect(f)['encoding'])
# with open('/Users/apple/PycharmProjects/get_movies/BeautifulSoup/regular_html.txtx','rb') as f:
# #     file = f.read().decode('utf-8')
# # doc = pq(url='https://cuiqingcai.com')
# # doc_html = pq(filename='/Users/apple/PycharmProjects/get_movies/BeautifulSoup/university_ranking_2020.txt')
#
# # print(doc('title'))
# # print(type(doc))
#     a = unicode(f.read(),'utf-8')
#     print(a)

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
'cookie': '_zap=93d871ca-fcc3-495d-8fa1-6e6f947fd8d4; _xsrf=CzRjEjR6EhsuKZk38XBbMS1GIRByA3aT; d_c0="APDQWHuhORKPTsGCZYAOnltgnd1mIj_tRhw=|1605885182"; capsion_ticket="2|1:0|10:1605885183|14:capsion_ticket|44:YWM2OTNiMzQ2MzZkNGI5ZTllN2JmZjdlYzU3ZDZkZDA=|033c12e3e1ee11ffc044b55319c595aece7d319ed494d57ab748ed564e8b3301"; z_c0="2|1:0|10:1605885399|4:z_c0|92:Mi4xMmZ1ZEJBQUFBQUFBOE5CWWU2RTVFaWNBQUFDRUFsVk4xMnJmWHdDR3FTUm5fRkJWc2tJWXNmSE1kOC1fSkdOV25R|59da082a9f6d246796b693ec083325347baf56ff47465a49b8113c55aed83a91"; tst=h; tshl=; q_c1=e7a82394852a4600957454a2f4d6d741|1607347088000|1607347088000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1607342863,1607347072,1607347124,1608032777; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1608032777; SESSIONID=NXjFAaZ9NyVXDRvjHKWZznnz8KSJcMkEGb8CgG2N5DN; JOID=U1EUB0pdG8RIGiZOV1jzkk_zLcxGG0urC1tPHGsTapoVW3QwNUq0HBISJkNXbq7md498pzIUFs5t6cJk6Jk1c0k=; osd=WlAcB0JUGsxIEi9PX1j7m077LcRPGkOrA1JOFGsbY5sdW3w5NEK0FBsTLkNfZ6_ud4d1pjoUHsds4cJs4Zg9c0E=; KLBRSID=37f2e85292ebb2c2ef70f1d8e39c2b34|1608032824|1608032775'
}
url = 'https://www.zhihu.com/explore'
html = requests.get(url,headers = headers)
# with open('pyquery_zhihu.txt','a') as f:
    # f.write(html.text)
doc = pq(filename='pyquery_zhihu.txt')
print(doc('title'))


