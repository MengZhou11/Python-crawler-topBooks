#学习使用sqlite

import sqlite3

#1.创建或者打开数据库
conn = sqlite3.connect("test.db")

#2.创建数据库中的不表格sheet
#获取游标
c = conn.cursor()
#正常用两个''如果是语句用三个'''
sql = '''
CREATE TABLE COMPANY
(ID int primary key not null,
name text not null,
age int not null,
address char(50),
salary real);
'''
#c.execute(sql)  #执行sql语句

#2.插入数据
sql2 = '''
insert into COMPANY(ID,name,age,address,salary) values
(1, 'Meng',26,"Beijing",8000);
'''
sql3 = '''
insert into COMPANY(ID,name,age,address,salary) values
(2, 'Zhou',26,"Beijing",5900);
'''

# c.execute(sql2)
# c.execute(sql3)

#3. 查找数据
sql4 = "select id, name ,age, address,salary from company"
data = c.execute(sql4)

for row in data:
    print("id: ",row[0])
    print("name: ",row[1])
    print("age: ",row[2])
    print("address: ",row[3])
    print("salary: ",row[4],"\n")



conn.commit()  #提交数据库操作
conn.close()   #关闭数据库

