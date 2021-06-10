from lxml import etree


a = open('zhuhu_hot.txt','rb')
f = a.read()
html = etree.HTML(f)
pattern = '//div[@class="HotList-list"]/section[@class="HotItem"]/div[@class="HotItem-content"]/a/@title'
result = html.xpath(pattern)

f = open('time.txt','a')
for a in range(len(result)):
    f.write('%s.%s\n' %(a+1,result[a]))
