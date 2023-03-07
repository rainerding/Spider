import requests

# 图片的url
# url = 'https://www.baidu.com/img/bd_logo1.png'

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# # 响应本身是一张图片，并且是二进制类型
# response = requests.get(url, headers=headers)

# print(response.content)
# print(response.request.headers)

# 以二进制+写入的方式打开文件
# with open('baidu.png', 'wb') as f:
#     # 写入 response.content bytes二进制类型
#     f.write(response.content)


# proxies = {
#     "http": "http://101.200.127.149:3129",
#     }

# response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=3)
# print(response.text)

# url = 'http://www.baidu.com'

# response = requests.get(url)
# print(type(response.cookies))

# # 使用方法从cookiejar中提取数据
# cookies = requests.utils.dict_from_cookiejar(response.cookies)
# print(cookies)

# url = 'https://www.12306.cn/mormhweb/'
# response = requests.get(url, verify=False, timeout=3)
# print(response)

# 使用 timeout 实现超时报错
# 使用 retrying 模块实现重试


from retrying import retry

headers = {}

# 最大重试3次，3次全部报错，才会报错
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    # 超时的时候会报错并重试
    response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response

def parse_url(url):
    try: #进行异常捕获
        response = _parse_url(url)
    except Exception as e:
        print(e)
        #报错返回None
    return response