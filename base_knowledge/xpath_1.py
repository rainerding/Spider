import re
import requests

# 目标网址：https://www.qqtxt.cc/list/1_2.html
# 获取到当前网页上更新列表里的所有小说名字(10页)
url = 'https://www.qqtxt.cc/list/1_2.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
response = requests.get(url,headers=headers)
response.encoding='gbk'
print(response.text)
with open('2.txt','wb') as f:
    f.write(response.text.encode('utf-8'))

from lxml import etree

html = etree.HTML(response.text)
ret_list = html.xpath('xpath字符串')

