import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq


def get_html():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    # 'cookie': '_zap=93d871ca-fcc3-495d-8fa1-6e6f947fd8d4; _xsrf=CzRjEjR6EhsuKZk38XBbMS1GIRByA3aT; d_c0="APDQWHuhORKPTsGCZYAOnltgnd1mIj_tRhw=|1605885182"; capsion_ticket="2|1:0|10:1605885183|14:capsion_ticket|44:YWM2OTNiMzQ2MzZkNGI5ZTllN2JmZjdlYzU3ZDZkZDA=|033c12e3e1ee11ffc044b55319c595aece7d319ed494d57ab748ed564e8b3301"; z_c0="2|1:0|10:1605885399|4:z_c0|92:Mi4xMmZ1ZEJBQUFBQUFBOE5CWWU2RTVFaWNBQUFDRUFsVk4xMnJmWHdDR3FTUm5fRkJWc2tJWXNmSE1kOC1fSkdOV25R|59da082a9f6d246796b693ec083325347baf56ff47465a49b8113c55aed83a91"; tst=h; tshl=; q_c1=e7a82394852a4600957454a2f4d6d741|1607347088000|1607347088000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1607342863,1607347072,1607347124,1608032777; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1608032962; SESSIONID=bvpEEYONbswGK87JOGS8k7wbY6gY729RFfTuYsWrF4B; JOID=VV8VAU4nq-mu-0M4PCJJuKEXSLAqRdqb7LwacHBH2Jnrt3kPcYktMfT5RD05RfV4skSnsa3QBuih80t8sprMgws=; osd=UFsXAUgir-uu_UY8PiJPvaUVSLYvQdib6rkecnBB3Z3pt38KdYstN_H9Rj0_QPF6skKita_QAO2l8Ut6t57Ogw0=; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1608352685|1608352677'

    url = 'https://www.zhihu.com/explore'
    html = requests.get(url = url,headers = headers).text

def prettfyy():
    soup = BeautifulSoup(html,'lxml')
    msg = soup.prettify()
    with open('zhihu_find.txt','wb') as f:
        f.write(msg.encode('utf-8'))


f = open('zhihu_find.txt',rb)
f.read()
doc = pq(f)





# doc = pq(url = 'https://www.zhihu.com/explore')
# print(doc)


# doc = pq(html)
# items = doc('.ExploreCollectionCard-contentList').text()
# print(items)



    # question = item.find('h2').text()
    # author = item.find('.author-link-line').text()
    # answer = pq(item.find('.content').html().text())
    # print(question)
