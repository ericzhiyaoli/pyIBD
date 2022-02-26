import openpyxl
import requests
 
wb = openpyxl.load_workbook(input("输入存放url链接的Excel电脑路径")) #输入存放url链接的Excel电脑路径，可以修改
sheet = wb[input("输入excel的sheet页的名称")] #excel的sheet页，可以修改
 
for i in range(100000000000000000): #excel中数据的行数，我这里是30条，可以修改
    name = sheet['A'+str(i+1)].value##此为PDF的命名，名字在表中A列
    url = sheet['B'+str(i+1)].value##PDF链接在表中B列，根据实际情况做更改
    pdf = open(str(name)+'.pdf','wb')
    res = requests.get(url)
    for chunk in res.iter_content(100000):
        pdf.write(chunk)
    pdf.close()
