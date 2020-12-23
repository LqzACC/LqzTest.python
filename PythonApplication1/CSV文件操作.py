import csv
from datetime import datetime
#filepath='C:\\360驱动大师目录\\sitka_weather_2014.csv'
filepath='D:\\代码\\python块包\\pcc-master\\chapter_16\\death_valley_2014.csv'
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)
    #(next(reader)返回一个全局变量)

"""
for index,column_header in enumerate(head_row):
    print(index,column_header)

date,high,low=[],[],[]
for arrange in reader:
    #(从当前行开始，由于前边使用了next，此时从第二行循环)(此时是字符串列表)
    try:
        dtime=datetime.strptime(arrange[0],'%Y-%m-%d')
        htempature=int(arrange[1])
        ltempature=int(arrange[3])
    except ValueError:
        print('not found data,please,check your code')
    else:
        date.append(dtime)
        high.append(htempature)
        low.append(ltempature)
print(date,high,low)
"""