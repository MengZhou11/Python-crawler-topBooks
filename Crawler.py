#codeing = utf-8
#Meng Zhou
#2021.06.06
import re
import sys  #网页解析，获取数据
from bs4 import BeautifulSoup  #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定url 获取网页数据
import xlwt  #进行Excel操作
import sqlite3  #进行sqllite操作数据库

def main():
    # getData(baseurl)
    # saveData(savePath)
    # askURL("https://movie.douban.com/top250?start=")
    path = "top250Movies.xls"
    baseurl = "https://movie.douban.com/top250?start="
    #爬取网页
    datalist = getData(baseurl)
    saveData(datalist,path)
    #影片详情链接

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

    return html




#爬取网页
def getData(baseurl):
    datalist = []
    findLink = re.compile(r'<a href="(.*?)">')  #找到每一个电影链接
    findImgScr = re.compile(r'<img.*src="(.*?)"',re.S) #re.S是忽略换行符
    findTitle = re.compile(r'<span class="title">(.*)</span>') #找到电影title
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  #评分信息
    findJudge = re.compile(r'<span>(\d*)人评价</span>')  #多少人评价
    findIntro = re.compile(r'<span class="inq>">(.*)</span>')  #概况
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S) #影片相关内容

    # 左闭右开 从0到249
    for i in range(0,10):
        url = baseurl + str(i*25)  #一次性获取25条内容  共有10页
        html = askURL(url)   #保存获取到的网页内容
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div',class_="item"):  #查到找的东西放到一个list里面 class需要加下划线,class_="item"
            #print(item)
            data =[]  #保存一个movie的所有信息
            item = str(item) #把item变成string
            #添加电影link
            link = re.findall(findLink, item)[0]  #每页里面有2个符合的 只提取第一个
            data.append(link)
            #添加电影图片
            imgSrc = re.findall(findImgScr, item)[0]
            data.append(imgSrc)
            #添加电影名
            titles = re.findall(findTitle, item)  #片名也许有1个或2个
            if(len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)  #add 中国电影名
                etitle = titles[0].replace("/","")
                data.append(etitle)  #add 英文电影名
            else:
                data.append(titles[0])
                data.append('')  #如果没有英文电影名 把这个留空
            #添加评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            #添加评价人数
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            #添加概述
            intro = re.findall(findIntro, item)
            if len(intro)!=0:
                intro = intro[0].replace("。", "") #去掉句号
                data.append(intro)
            else:
                data.append("")
            #添加相关内容
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?',"",bd) #去掉br
            bd = re.sub('/',"",bd) #替换
            data.append(bd.strip())  #strip是用来去掉空格
            #把一个data放进datalist里面
            datalist.append(data)
    #print(datalist)
    return datalist


#3.保存数据excel
def saveData(datalist,savePath):
    print("saving..")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet=book.add_sheet('top250movies',cell_overwrite_ok=True)
    col = ("Link","Image","Movie title","movie title2", "Rating","Num of Rating","Introduction","More info")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print(i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1, j, data[j])
    book.save(savePath)


if __name__ == "__main__":   #执行程序
    main()