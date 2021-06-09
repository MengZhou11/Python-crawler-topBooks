#codeing = utf-8
#Meng Zhou
#2021.06.06

import sys  #网页解析，获取数据
from bs4 import BeautifulSoup  #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定url 获取网页数据
import xlwt  #进行Excel操作
import sqlite3  #进行sqllite操作数据库

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist = getData(baseurl)
    getData(baseurl)
    savePath = ".\\top250.xls"  #当前文件
    saveData(savePath)
    #askURL("https://book.douban.com/top250?start=")

#爬取网页
def getData(baseurl):
    datalist = []
    # 左闭右开 从0到249
    for i in range(0,1):
        url = baseurl + str(i*25)
        html = askURL(url)   #保存获取到的网页内容
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_="item"):  #查到找的东西放到一个list里面 class需要加下划线
            print(item)

    return datalist

#得到指定一个url网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    }  #告诉douban网站 我不是爬虫  模拟浏览器头部信息 伪装

    request = urllib.request.Request(url=url, headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    #return html


#3.保存数据
def saveData(savePath):
    print("saving..")


if __name__ == "__main__":   #执行程序
    main()