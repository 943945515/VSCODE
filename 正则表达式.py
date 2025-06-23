import re
# re.match(pattern,string,flags)
#pattern:匹配的正则表达式
#string:匹配的字符串
#flags:标志位，用得很少

res = re.match("冰","冰冰yyds")
print(res)
print(res.group())
# 注意：match是从开始位置匹配，匹配不到就没有
   
res = re.match(r"<(\w*)>\w*</\1>",'<html>login</html>')    
print(res.group())

res = re.match(r'www(\.)\w*\1(com|cn|org)','www.baidu.com')
print(res.group())



li = ['www.baidu.com','www.python.org','http.jd.cn','www.py.en','www.abc.cn']

for i in li:
    res = re.match(r'www(\.)\w*\1(com|cn|org)',i)
    if res:
        print(res.group())
    else:
        print(f'{i}这个网址有错误')



res = re.sub("\d","2","这是这个月的第30天",1)
print(res)


res = re.match("m*?","mmmmm")
print(res.group())


res = re.match(r"\\","\game")
print(res.group())
#正则表达式中，匹配字符串中的字符\需要\\表示一个\