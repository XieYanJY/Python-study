import json

msg = [{'name':'欧阳修','poem':'人生自是有情痴，此恨无关风与月','bir':2020}]

with open('ouyang.json','w') as f:
    f.write(json.dumps(msg,indent=2,ensure_ascii=False))

str = '''
[{"name":"欧阳修", 
"poem":"人生自是有情痴，此恨无关风与月",
"bir":2020}]'''
date = json.loads(str)
print(date)
print(type(date))

# date2 = json.loads(msg)
# print(date2)


