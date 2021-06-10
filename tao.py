import requests
import re




# kv = {'user-agent': 'Mozilla/5.0',
#       'cookie':' isg=BE1Nm_RZERlif7U0gsG_Y38NXm_HKoH8Uxals4_SiORThm04V3m9zJaQ8JrgXZm0; l=eBTKiignj_IcnVt-BOfa-urza77ThIdYYuPzaNbMiOCPODCB5PH5W6gSveL6Cn1VhsQWR3o7A-48BeYBcWPEnxvtIosM_iHmn; tfstk=czy1BRgBVreFrhv2DlseQvbX-IMAZLpsYGg3f5k3yA8Mzja1MT0zHoADJkysx; cna=RWu7GJWULFsCAXWIQoxJei2p; mt=ci=0_0; tracknick=; _m_h5_tk=085cbc6b5d42e2c0c7d9f7070fd0c2b4_1614101279934; _m_h5_tk_enc=892b270c516bca5153a4452d9f8c0d9e; thw=cn; _tb_token_=fe768e73148eb; cookie2=1974f939e5915be812a80896437e1c6c; t=434920ef67a0b8cd9955dd2cebfc2edf; _samesite_flag_=true; xlly_s=1'}
def getHTMLText(url):
    kv = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.3 Safari/605.1.15',
        'Cookie': 'isg=BD4-QYWA0tzi7gb5ZfSchhDAjVKAfwL5zAv2vuhHqgF8i95lUA9SCWTtA9dHqPoR; l=eBTKiignj_IcnMmxBO5BEurza779EQA08kPzaNbMiInca6s5TFtgtNCIPxvX7dtfgtfDWetrVkw0yREvyTUZ1xDDBeD_7qCl8Yv6-; tfstk=cP_5Be9j19Q2rWuE9_NqzE4ejuLhaMuWg79cNg80br2Uwz6JMsekQwCnxxCVPIf..; uc1=cookie14=Uoe1hgbYeyzW0A%3D%3D&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=false&pas=0&cookie21=W5iHLLyFeYZ1WM9hVnmS; mt=ci=94_1; _cc_=VT5L2FSpdA%3D%3D; _l_g_=Ug%3D%3D; _nk_=tb%5Cu5927%5Cu817F%5Cu9AA8; _tb_token_=fe768e73148eb; cookie1=B0f0ceK8H%2B14us6u%2BQi6nt6%2FY126t8E06%2F8rDatubXs%3D; cookie17=UUGlSinwBV6A5A%3D%3D; cookie2=1974f939e5915be812a80896437e1c6c; csg=06ec7a53; dnk=tb%5Cu5927%5Cu817F%5Cu9AA8; existShop=MTYxNDA5NTYwNg%3D%3D; lgc=tb%5Cu5927%5Cu817F%5Cu9AA8; sg=%E9%AA%A809; sgcookie=E100LcgApVht59WYWFJx6U1IR%2FjRnL20247i2uC00VQqYU9S8EESxgmh3gugPDe%2FuAmq1SygMZsbm2H3L5CqIz0%2BRA%3D%3D; skt=53838f0af8478df4; t=434920ef67a0b8cd9955dd2cebfc2edf; tracknick=tb%5Cu5927%5Cu817F%5Cu9AA8; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUGlSinwBV6A5A%3D%3D&vt3=F8dCuASh46%2BWn5S5q0M%3D&nk2=F5TBI2Jbi20%3D; uc4=nk4=0%40FY6KpDSLFLjKSZkh9f5WKS4PVQ%3D%3D&id4=0%40U2OSXcxS5Yuzz2GmFATt3ARjo6QM; unb=2974172750; cna=RWu7GJWULFsCAXWIQoxJei2p; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; enc=NsyRjii4WV79XDnrjMvWJAB9kN4%2BvNPmKGpJsyKt%2FtV9E9nhN7KW8m%2Bz06NdTBILYxTutGwn62TVWqsdj134wg%3D%3D; _m_h5_tk=085cbc6b5d42e2c0c7d9f7070fd0c2b4_1614101279934; _m_h5_tk_enc=892b270c516bca5153a4452d9f8c0d9e; _samesite_flag_=true; xlly_s=1'}

    # try:
    r = requests.get(url, headers=kv)
    # r.raise_for_status()
    # r.encoding = r.apparent_encoding
    print('1')
    # print(r.text)
    print(r.status_code)
    return r.text
    # except:
    #     print('网页没撞到')
    #     print(r.status_code)
    #     return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
        print('解析完成')
    except:
        print("解析失败")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
    print('输出')


def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44 * i)
            print('访问网址')
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            print('失败')
    printGoodsList(infoList)


main()