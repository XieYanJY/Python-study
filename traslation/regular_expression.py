import re
def ip():
    a = '254.1.1.256'
    res = re.search('(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',a)
    # msg = re.search('(((2(5[0-5]|[0-4]\d))|([0-1]?\d{1,2}))\.){3}((2(5[0-5]|[0-4])\d)|[0-1]\d{1,2})',a)
    mis = re.search('((2(5[0-5]|[0-4])\d|[0-1]?\d{1,2})\.){3}(2(5[0-5]|[0-4])\d|[0-1]?\d{1,2})',a)
    try:
        print(res,mis)
    except reason as e:
        print(e)
# |
# print(re.search('C|D|[cd]','constitution'))

# ^

# $

# [.]

# *  匹配0次或多次，{0,}
# ?  匹配0次或1次，{0,1}
# +  匹配1次或多次，{1,}
# # \b 匹配单词边界，单词被定义为Unicode的字母数字或下横线字符
# print(re.findall(r'\bcon\b','con!stitution.con!tinue (conu)+conter'))
# # \B 匹配非单词边界
# print(re.findall(r'\Bcon\B','con stitution+continue!count(qconqu)'))
# \d
# \D
# \s 空白字符
# \S 非空白字符
# \w 单词，字符，数字，下横线
# 、W
# 非捕获组 ？：该组捕获的字符串不会在后面获取

#
def wide(num):
    p = r'[1-9]?\d$|100$'
    for i in range(0,num):
        i = str(i)
        print(re.findall(p,i))

wide(101)

p = r'^[1-9]?\d$|100$'
print(re.findall(p,'101'))