import re

f = open('/Users/apple/PycharmProjects/get_movies/BeautifulSoup/regular_html.txtx','rb')
print(type(f))
# print(type(f.read()))
html = f.read().decode('utf-8')
print(type(html))
print(f)
#
pattern_title = re.compile('title="(.*?)">')
pattern_expert = re.compile('<p class="HotItem-excerpt">\s*(.*?)\s*</p>')
pattern_link = re.compile('href="(.*?)"')
title = re.findall(pattern_title,html)
expert = re.findall(pattern_expert,html)
if expert == ' ':
    expert.append('无')
# else:
#     expert.append()
link = re.findall(pattern_link,html)


# print(title)
# # print(len(title))
print(expert)
print(len(expert))
# # print(link)
# print(len(link))