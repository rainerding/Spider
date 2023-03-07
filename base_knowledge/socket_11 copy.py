import re
import socket

url = 'https://pic.netbian.com/uploads/allimg/220211/004115-1644511275bc26.jpg'

client = socket.socket()

client.connect(('pic.netbian.com', 80))

http_res = 'GET ' + url + ' HTTP/1.0\r\nHost: pic.netbian.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36\r\n\r\n'

client.send(http_res.encode())
result = b''

data = client.recv(1024)


while data:
    result += data
    data = client.recv(1024)

print(result)

images = re.findall(b'\r\n\r\n(.*)', result, re.S)

with open('hhh.png', 'wb') as f:
    f.write(images[0])