import socket
import re

# 获取到资源地址
url = "http://image11.m1905.cn/uploadfile/2021/0922/thumb_0_647_500_20210922030733993182.jpg"
# 创建套接字对象
client = socket.socket()
# 创建连接 connect的内容是host(主机和端口号)
client.connect(('image11.m1905.cn', 80))
# 构建http请求 请求类型+url+user-agent(浏览器名称)
http_res = 'GET ' + url + ' HTTP/1.0\r\nHost: image11.m1905.cn\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36\r\n\r\n'
# 发送请求
client.send(http_res.encode())
# 建立一个二进制对象用来存储我们得到的数据
result = b''
data = client.recv(1024)
# 循环接收响应数据 添加到bytes类型
while data:
    result += data
    data = client.recv(1024)
print(result)
# 提取数据
# re.S 使 . 匹配包括换行在内的所有字符 去掉响应头
images = re.findall(b'\r\n\r\n(.*)', result, re.S)
print(images[0])
# 打开一个文件，将我们读取到的数据存入进去，即下载到本地我们获取到的图片
with open('xjj.png', 'wb') as f:
    f.write(images[0])
