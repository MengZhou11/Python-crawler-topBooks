#正则表达式 学习
#正则用来判断字符串是否符合一定标准


import re

#方法1：有个具体的规定
#AA是正则表达式 来验证其他的字符串
pat = re.compile("AA")
#search字符串是被校验的内容 显示找到的位置靠前的
print(pat.search("ABCAADDCCAAA"))

#方法2： 没有模式对象
m = re.search("asd", "Aasd")
print(m)

#方法3：找到所有符合规定的字符串 放到一个[]list里面
print(re.findall("a", "ASDaDFGAa"))
print(re.findall("[A-Z]","ASDaDFGAa"))
print(re.findall("[A-Z]+","ASDaDFGAa"))

#另外一种叫sub 替换
print(re.sub("a", "A", "abcdcasd"))

#放r在被比较的字符串前面
a = r"\aabd-\'"
print(a)