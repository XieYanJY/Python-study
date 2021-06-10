import requests
from bs4 import BeautifulSoup

def get_html(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    html = requests.get(url,headers)
    html.encoding = 'utf-8'
    with open('university_ranking_2020.txt','a') as f:
        f.write(html.text)
    res = html.text
    return res
    # print(html.headers['content-type'])
    # print(html.text)
    # print(html.encoding)

def parse_html(res):
    html = open('university_ranking_2020.txt')
    soup = BeautifulSoup(html, 'lxml')
# print(soup.text)
# print(soup.name)
# title = soup.span.string

# print(soup.td.string)
# print(soup.find_all(soup.title.string))  #错误
# print(soup.div.attrs)
    #获取数据列表，tag，bs4
#     a = soup.find_all(name = 'a')
# # print(a)
#     type1 = []
#     for i in a:
#         if i.string == None:
#             pass
#         else:
#             type1.append(i.string)
#获取数据列表
    school = soup.find_all(name = 'td')
    schools = []
    for i in school:
        schools.append(i.string)
    return schools
# print(school1)

# schools = []
# for s in school1:
#     print(type(s))
#     # s.replace(' ','')
#     schools.append(s)
#
# print(schools)

def print_list(schools):
    n = 1
    while n <= (len(schools)-3):
        if (n)%3 == 1:
            print('%s\t%s\t%s\n'%(schools[n+2],schools[n+1],schools[n]))
        else:
            pass
        n += 3

def main():
    if __name__ == '__main__':
        url = 'https://www.eol.cn/e_html/gk/dxpm/index.shtml'
        print_list(parse_html(get_html(url)))

main()


# print(soup.div.contents)


