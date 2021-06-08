#这个文档用来理解如何获取数据
import re
from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser") #html.parser是解析器

# print(bs.title)
# print(bs.a)
#
# print(type(bs.head))
#
# #1. Tag 标签及其内容 拿到第一个出现的
# print(bs.title.string) #只看内容
# print(type(bs.title.string))
#
# print(bs.a.attrs)
# print(type(bs)) #也可以直接打印bs

# print(bs.head.contents)
# print(bs.head.contents[1])

#文档遍历 核心部分 实际应用
#文档搜索

#find_all()
#字符串过滤 会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")


#！！！！重点来了！！正则表达式搜索：使用search()方法来匹配内容
#正则表达式搜索 不管是标签还是内容 只有含有搜索关键词的内容全部展示出来
# t_list=bs.find_all(re.compile("a"))


#方法1：传入一个函数method 按method要求搜索
# def name_is_exits(tag):
#     return tag.has_attr("name")
#
# t_list=bs.find_all(name_is_exits)
# print(t_list)


#方法2：keyword参数
# t_list=bs.find_all(id="head")
# t_list=bs.find_all(class_=True)  #有class的所有内容/标签
# t_list=bs.find_all(href="http://news.baidu.com")
# print(t_list)


#方法3：text参数
# t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123","地图","贴吧"])
# t_list = bs.find_all(text=re.compile("\d"))  #\d表示包含数字的内容 re是正则表达式library
# print(t_list)


#方法4：limit参数
# t_list=bs.find_all("a", limit=3)  #只显示3条
# print(t_list)


#css选择器
print(bs.select('title'))  #通过标签查找
print(bs.select('.mnav'))  #通过类名查找
print(bs.select('#u1'))    #通过id查找
print(bs.select("a[class='bri']"))   #通过属性查找
print(bs.select("div>a"))  #通过子标签来查找
print(bs.select(".mnav~ .bri"))