# from bs4 import BeautifulSoup
#
# f = open('/Users/apple/PycharmProjects/get_movies/xpath/zhuhu_hot.txt','rb')
# soup = BeautifulSoup(f, 'lxml')
# print(soup.prettify())
# print('\n')
# print(soup.title.string)



# dixt = {'ko':'llkk','kv':'kp'}
# print(len(dixt))
# for k,v in dixt.items():
#     print(k+':'+dixt[k])
#
# def h():
#     a = 1,2
#     return a
#
# print(h())


# robot协议
from urllib.robotparser import RobotFileParser
# 取消全局证书验证
import ssl
# content = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

re = RobotFileParser()
re.set_url('https://www.zhihu.com/robots.txt')
re.read()
print(re.can_fetch('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36','https://www.zhihu.com/'))
print(re.can_fetch('Baiduspider-image','https://www.zhihu.com/'))

# print(re.read())
