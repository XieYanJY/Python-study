import requests
from lxml import etree
from bs4 import BeautifulSoup
import re
# from pyquery import PyQuery as pq
import time


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15',
        'Cookie':'KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1619519062|1619519044; tshl=; tst=h; JOID=UV0TCkOzpdS3Dfn4TbnIiFgIvWVZ-MqM9z-9wjvvwIP3ZsW6If9PXd0A_PRDCGgDxQQf5RN1lV2o3y1G3gzxTVs=; SESSIONID=MlWA9B9yWcTOj7Do1UMeJ4yq1WGJ08te4yj1t4uFIGw; osd=Wl8SAE24p9W9A_L6TLPGg1oJt2tS-suG-TS_wzHhy4H2bMuxI_5FU9YC_f5NA2oCzwoU5xJ_m1aq3idI1Q7wR1U=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1619519046; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1617158296,1618404425; captcha_ticket_v2="2|1:0|10:1619426677|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfdkl3ZXN0eDd1dzE0YjFnbFJZaTk0dnBPVGlUcUN6MS0uOUlySEkySktvZElsYzZlaC1FME9aUi5fLi1BODhaZXVMZkZLN0NCbTJwX1ZMLTRqYXZXRGU4NTI1N2N0RDF1ZjZ3aWVGUnJmSTJ3cEtEbUZ3UmlQYlI5VmpTWGQwYVNha2xzV1dhXzc4RldJTk5ueFRBa1BfWE9LTkJ5Y25CTEZjdTR6RGdfamNQRmVRUC53LWlTclB6YmwxckpYTzlwcHRlejBqS25TQnVja1VtMkJSZVVhV2I3cVFES0JFWDlsbDVIaW5wR2ltUExsMVRTdmpOcmN1SXJjSnVtQW9aRjRHV2g4MUw2NHFzaWwya25xVWhjdTRMYlZ1Y1dfcVZNSWt0NHd3YjUyeWk4d3FvYUNfblQwSWxoaHQxQW5zd2NsdkZNS0Z5bmcwSmZISmNvVFJFWldOWGFWbkFvemdvd3paZ2M4T21ESW5nN1ctcGFmUG9XYUVKQmNKb1U4bGZXc1ZITno1V3N4NmlJYXF1SE9fX214Y1o2azhJNTZzV2VRSFRwZEk4Qms5eEw0aDBPNk56QzJVUkFRVVpuNzQtS0lpMW13RG5sOHYyMGl4WHVuVUcyOFI1WUdqVmtYS2dVblN2U2FUN0d6eGpuVm4wbGFkTWZkSVIySVdOMyJ9|06771aa9e4f2aa08a68da7b688cdfce21a2584246e20e3a93b6ad22fcf46768d"; z_c0="2|1:0|10:1619426677|4:z_c0|92:Mi4xMmZ1ZEJBQUFBQUFBTU5GMUFLSnNFU1lBQUFCZ0FsVk5kY3R6WVFBRVk4LXRYZ01RR3Jncm80WHpSSE84REVhblN3|e9c0c31e34edae6be64dedf8209b934bb12c7383e58c03db47565828838821d8"; YD00517437729195%3AWM_TID=x%2BOrk09PM3xAVAAFFVZ7hC0LNuO0MhEE; captcha_session_v2="2|1:0|10:1619426666|18:captcha_session_v2|88:cmhaZHA3VUxtcndXUjQydHlDVnRkT1JWdHRoRHZiVEJ6ZWdPaTBqWjUvTmlqMnQ5YUxGZ3dNbThCNFBWQTdFVQ==|084c8bf3d3d50f10a06e52e2b611d582343697e24ff187b49b48e9a7c0dbfc88"; _9755xjdesxxd_=32; gdxidpyhxdE=0uYyv4lzWTKyL9LmNP1WJO%2FevsXsQbHgoMRQ4XRG0L8QNrH%2FR5T68s8gqREZagcr1U5Kp7IPVfS%5Cws5ewPiwVah%2BhELIHniNNXDr5VRsgC3IWxgMRQcx4ySBW%5CESG%2BDgp67NY8V%2BTV1JLuyM6W8VcliO%5Cc7qyt%5C7z%5C9TlJw71ge7XuJu%3A1619427328251; YD00517437729195%3AWM_NI=X12nHEbCCW20YzlC8MJNNB7GWTNyqAjMm%2BH46TaOnOefHydbo5yygto%2BryyLZmXWjCKLuXjrj8YdHSvIIjtfBcRZfjMVyX01f%2BT1ISrO524i0%2FQmRlwhdero35A7zZAkUnY%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee9bbc399789bca6db6e9bb48eb2d44f938f8fbaae3bb089fdb5d13f9ab99695c52af0fea7c3b92a9ceffe8fcb4fa29d8db8b13c9ba6a4a4bb478a9282a3b64d958c829af44baa93a3cccb40f68cafb0ed45a7ba889ae76aadebb79ae680adf5be9afc489ab398b8e9498994bbb9e97aaae89785cb59b697878bf76e82bd9ebbe5628f8ab7b9b33ba6f59cd2cc59b291fbd3b763f4f19f8ed168b5b8ac86f165f1eb8fd8f95283b59b8fdc37e2a3; __snaker__id=IjhG1cGV0Im1ddur; q_c1=9eeb558ae4094e93b6ff3872393f59bb|1614579208000|1592140203000; d_c0="ADDRdQCibBGPTrVHiqxEcDVf4cIF1OTmDe0=|1592128001"; _xsrf=BdWCCO40dzuNP6K9KWrkB17XWMr7H91m; _zap=6b9ca833-c7cb-4ef1-a57d-c6aab137f8aa'
    }

    # url = 'https://www.zhihu.com/hot'
    req = requests.get(url, headers = headers)
    print(req.status_code)
    req = req.text
    # print(req)
    return req


def Parse_html(req):
    # pattern = '//div[@class="HotItem-content"]/a/@title/text()'
    pattern_title = '//div[@class="HotList-list"]/section[@class="HotItem"]/div[@class="HotItem-content"]/a/@title'
    pattern_web = '//div[@class="HotList-list"]/section[@class="HotItem"]/div[@class="HotItem-content"]/a/@href'
    # pattern_excerpt = '//div[@class="HotItem-content"]/a/text()'
    html = etree.HTML(req)
    title = html.xpath(pattern_title)
    web = html.xpath(pattern_web)
    # print(len(web))
    # print(len(web))
    # print(title)
    # soup = BeautifulSoup(req,'lxml')
    # expert = soup.find('p').string
    # beautifulsoup
    # doc = pq(req)
    # expert_ = doc('p')
    # expert = []
    # for i in expert_.items():
    #     expert.append(i.text())
    # print(expert)
    # print(len(expert))

    result = title,web
    # print(title,web)
    # print(result)
    return result

# def catch_time():
#     t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     with open('catch_zhihuhot.txt','a') as T:
#         T.write(t+'\n')
#         print()
def get_expert(req):
    soup = BeautifulSoup(req,'lxml')
    msg = soup.find_all('div',class_="HotItem-content")
    expert = []
    pattern = re.compile('<p class="HotItem-excerpt">\s*(.*?)\s*</p>')
    # print(type(msg))
    for item in msg:
        item = str(item)
        expert_ = re.findall(pattern,item)
        if expert_ == []:
            expert.append('无')
        else:
            expert.append(expert_)

    # print('er')
    # print(expert)
    # print(type(expert))
    # print(len(expert))
    return expert



def list_content(result,expert):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(t)
    with open('catch_zhihuhot.txt', 'a') as f:
        f.write(t + '\n')
        # i = len(result[0])
        for k in range(len(result[0])):
            f.write('%s. %s\n\t%s\n\t%s\n' %(k+1, result[0][k],expert[k][0],result[1][k]))
        f.write('\n')
        # print('yes')

def main():
    if __name__ == '__main__':
        url = 'https://www.zhihu.com/hot'
        html = get_html(url)
        title_link = Parse_html(html)
        expert2 = get_expert(html)
        list_content(title_link,expert2)
        print('今日知乎热榜爬取成功！')

        # list_content(Parse_html(get_html(url)))
        # Parse_html(get_html(url))
        # get_expert(get_html(url))

main()

