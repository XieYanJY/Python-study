from bs4 import BeautifulSoup

f = open('regular_html.txtx','rb')
html = f.read()
soup = BeautifulSoup(html,'lxml')


# def fing_p(soup):
#     msg = soup.find_all('p')
#     print(type(msg))
#     for i,item in enumerate(msg,start=1):
#         print('%s.%s\n' %(i,item.string))


def find_attrs(soup):
    msg = soup.find_all('div',class_='HotItem-content')
    # print(len(msg))
    import re
    compile_link = r'href="(.*?)"'
    compile_title =r'title="(.*)">'
    compile_expert = r'<p class="HotItem-excerpt">\s*(.*?)\s*</p>'
    link_l = []
    title_l = []
    expert_l = []

    for i in msg:
        i = str(i)
        link = re.findall(compile_link,i)
        link_l.append(link)
        title = re.findall(compile_title,i)
        title_l.append(title)
        expert = re.findall(compile_expert,i,re.S)
        if expert == []:
            expert_l.append(' ')
        else:
            expert_l.append(expert)

    # print(link_l,title_l,expert_l)
    # print(len(expert_l))
    result = title_l,expert_l,link_l
    # for i in result:
    #     print(i)
    print(200)
    return result



def parse_html(result):
    print(len(result[0]))
    for i in range(len(result[0])):
        print('%s. %s\n\t%s\n\t%s' %(i+1,result[0][i][0],result[1][i][0],result[2][i][0]))
        #                                        ,


parse_html(find_attrs(soup))
# find_attrs(soup)

# print(msg)


# with open('regular_html.txtx','a') as reg:
#     reg.write(r)

# print(soup.text)
# print(soup.name)
# print(soup.style.string)
# print(soup.head)
# print(soup.p)#选中第一个节点

# print(soup.title.name)
# print(soup.title.string)
# print(soup.p.attrs)
# print(soup.p.name)
# print(soup.p.string)
# print('\n')
#
# print(soup.text)

# print(5%3)
# My_list = ["aaa, 100 0, we", "bbb, we, qt", " I, love, you",'']
# print(type(My_list))
# New_list = []
# for i in My_list:
#     New_list.append(i.replace(" ",""))
#
# My_list = New_list
# print(My_list)
#
# b = [2,'m']
# for i in b:
#     print(type(i))
# ['aaa,1000,we', 'bbb,we,qt', 'I,love,you']
