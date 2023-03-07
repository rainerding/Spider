import re

# 使用match方法进行匹配操作
#result = re.match(正则表达式,要匹配的字符串)
# result = re.match('tuling','tuling.cn')
# # 获取匹配结果
# inf0 = result.group()
# print(inf0)

# ret = re.match('.','M')
# print(ret.group())

# ret = re.match('t.o','too')
# print(ret.group())

# ret = re.match('t.o','two')
# print(ret.group())

# 如果hello的首字符小写，那么正则表达式需要小写的h
# ret = re.match('h','hello python')
# print(ret.group())

# # 如果hello的首字符大写，那么正则表达式需要大写的h
# ret = re.match('H','Hello Python')
# print(ret.group())

# 大小写h都可以的情况下
# ret = re.match('[Hh]','hello Python')
# print(ret.group())
# ret = re.match('[Hh]','Hello Python')
# print(ret.group())
# ret = re.match('[Hh]ello Python','Hello Python')
# print(ret.group())

# # 匹配0到9第一种写法
# ret = re.match('[0123456789]Hello Python','7Hello Python')
# print(ret.group())

# # 匹配0-9第二种写法
# ret = re.match('[0-9]Hello Python','7Hello Python')
# print(ret.group())

# ret = re.match('[0-35-9]Hello Python','7Hello Python')
# print(ret.group())

# ret = re.match('[0-35-9]Hello Python','4Hello Python')
# print(ret)
# print(ret.group())

# \d
# 普通的匹配方式
# ret = re.match('嫦娥1号','嫦娥1号发射成功')
# print(ret.group())

# # 使用\d进行匹配
# ret = re.match('嫦娥\d号','嫦娥1号发射成功')
# print(ret.group())

# # \D
# match_obj = re.match('\D','f')
# if match_obj:
#     # 获取匹配结果
#     print(match_obj.group())
# else:
#     print('匹配失败')

# \s
# 空格属于空白字符
# match_obj = re.match('hello\sworld','hello world')
# print(match_obj.group())

# # \t 属于空白字符
# match_obj = re.match('hello\sworld','hello\tworld')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# \S 非空白
# match_obj = re.match('hello\Sworld','hello$world')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# match_obj = re.match('hello\Sworld','hello#world')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# \w 匹配非特殊字符中的一位
# match_obj = re.match('\w','A')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# \W 匹配特殊字符中的一位
# match_obj = re.findall('\W','#A#')
# # findall找所有，返回一个列表，没有就是空列表
# if match_obj:
#     print(match_obj)
# else:
#     print('匹配失败')

# sub替换
# match_obj = re.sub('\W','_','#A#')
# # findall找所有，返回一个列表，没有就是空列表
# if match_obj:
#     print(match_obj)
# else:
#     print('匹配失败')

# compile 编译
# match_obj = re.compile('\d',re.S)
# # findall找所有，返回一个列表，没有就是空列表
# if match_obj:
#     print(match_obj)
# else:
#     print('匹配失败')

# * 匹配前一个字符出现0次或者无限次，即可有可无
# 匹配出一个字符串第一个字母为大写字符，后面都是小写字母且这些小写字母可有了可无
# ret = re.match('[A-Z][a-z]*','M')
# print(ret.group())

# ret = re.match('[A-Z][a-z]*','MnnM')
# print(ret.group())

# ret = re.match('[A-Z][a-z]*','Aabcdef')
# print(ret.group())

# + 匹配前一个字符出现1次或者无限次，即至少有1次
# 匹配一个字符串，第一个字符是t,最后一个字符串是o,中间至少有一个字符
# match_obj = re.match('t.+o','two')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# ？匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# match_obj = re.match('https?','http')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# {m} 匹配前一个字符出现m次
# {m,n} 匹配前一个字符出现从m到n次
# 匹配出，8到20位的密码，可以是大小写英文字母、数字、下划线
# ret = re.match('[a-zA-Z0-9]{6}','12a3g45678')
# print(ret.group())

# ret = re.match('[A-Za-z0-9]{8,20}','1ad12f23s34455ff6632432424322')
# print(ret.group())

# ret = re.match('[A-Za-z0-9]{8,20}','1ad')
# print(ret.group())

# ^ 匹配字符串开头
# match_obj = re.match('^\d.*','3hello')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# # $ 匹配字符串结尾
# ret = re.match('.*\d$','hello6')
# print(ret.group())

# 匹配以数字开头中间内容不管以数字结尾
# match_obj = re.match('^\d.*\d$','3hdhdu7')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# 除了指定字符串以外的都匹配
# match_obj = re.match('[^aeiou]','h')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

"""------------------------------------------------------------------------------------"""

# 匹配分组
"""
| 匹配左右任意一个表达式
(ab) 将括号中字符作为一个分组
\num 引用分组num匹配到的字符串
(?P) 分组起别名
(?P=name) 引用别名为name分组匹配到的字符串
"""

# | 在列表中["apple", "banana", "orange", "pear"]，匹配apple和pear
# 水果列表
# fruit_list = ['apple','banana','orange','pear']
# # 遍历数据
# for value in fruit_list:
#     match_obj = re.match('apple|pear',value)
#     if match_obj:
#         print(f'{match_obj.group()}是我想要的')
#     else:
#         print(f'{value}不是我想要的')

# () 匹配出163、126、qq等邮箱
# match_obj = re.match('[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com','hello@163.com')
# if match_obj:
#     print(match_obj.group())
#     print(match_obj.group(1))
# else:
#     print('匹配失败')

# 匹配qq:10567这样的数据，提取出来qq文字和qq号码
# match_obj = re.match('(qq):([1-9]\d{4,10})','qq:10567')
# # match_obj = re.match('(qq):(\d{5,10})','qq:10567')
# if match_obj:
#     print(match_obj.group())
#     # 分组：默认是1一个分组，多个分组从左到右依次加1
#     print(match_obj.group(1))
#     print(match_obj.group(2))
#     print(match_obj.group(3))
# else:
#     print('匹配失败')

# \num 
# match_obj = re.match('<[a-zA-Z1-6]+>.*</[A-Za-z1-6]+>','<html>hh</html>')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# 匹配出www.tuling.cn
# match_obj = re.match('<([a-zA-Z1-6]+)><([A-Za-z1-6]+)>.*</\\2></\\1>','<html><h1>www.tuling.cn</h1></html>')
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# (?P) 分组起别名 大写的P
# (?P=name) 引用别名为name分组匹配到的字符串
# match_obj = re.match("<(?P<name1>[a-zA-Z1-6]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>", "<html><h1>www.tuling.cn</h1></html>")
# if match_obj:
#     print(match_obj.group())
# else:
#     print('匹配失败')

# 把字符串 title = '你好，hello，世界' 中的中文提取出来
# title = "你好，hello，世界"
# pattern = re.compile('[\u4e00-\u9fa5]+')
# result = pattern.findall(title)
# print(result)

"""------------------------------------------------------------------------------------------------------"""

# 目标网址：https://www.dns.com/login.html
# 获取到当前网址上的csrfToken 的值

import requests

# url = 'https://www.dns.com/login.html'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# # print(response.text)
# data = re.findall('    var csrfToken = ".*";',response.text)
# # data = re.findall('    var csrfToken = ".*?";',response.text)
# print(data)

# 目标网址：https://www.qqtxt.cc/list/1_2.html
# 获取到当前网页上更新列表里的所有小说名字(10页)
# url = 'https://www.qqtxt.cc/list/1_2.html'
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
# }
# response = requests.get(url,headers=headers)
# response.encoding='gbk'
# print(response.text)
# with open('2.txt','wb') as f:
#     f.write(response.text.encode('utf-8'))
