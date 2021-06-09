#学习如何将数据保存到excel里

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet =workbook.add_sheet('sheet1')
#行然后列 然后内容
# worksheet.write(0,0,'hello')
# #保存excel  注意这里是workbook
# workbook.save('student.xls')

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d *%d = %d" %(i+1, j+1,(i+1)*(j+1)))
workbook.save('math.xls')