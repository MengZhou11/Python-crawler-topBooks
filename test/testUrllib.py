#学习教程：https://www.bilibili.com/video/BV12E411A7ZQ?p=18&spm_id_from=pageDriver
#MENG ZHOU

import urllib.request

#获取get请求
# response = urllib.request.urlopen("https://www.baidu.com")
# print(response.read().decode('utf-8'))  #获取utf-8解码


#获取post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello" : "world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(response.read().decode("utf-8"))


#有超时处理exception，timeout
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01) #timeout按秒
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("Time out!")

#被发现是爬虫
# response = urllib.request.urlopen("http://www.baidu.com") #timeout按秒
# # print(response.status)   #出现http error 418是被发现爬虫了
# print(response.getheader("server"))


#如何解决被发现爬虫问题，更改user agent
# url = "https://httpbin.org/post"
# header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
# } #自己设定这个user agent让网站不发现我们在用爬虫
# data = bytes(urllib.parse.urlencode({'name': 'eric'}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=header, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))


url = "https://douban.com"
header={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))