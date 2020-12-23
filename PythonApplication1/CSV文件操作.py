import csv
from datetime import datetime
filepath='C:\\360驱动大师目录\\sitka_weather_2014.csv'
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)
    #(next(reader)返回一个全局变量)
for index,column_header in enumerate(head_row):
    print(index,column_header)

date,high,low=[],[],[]
for arrange in reader:
    #(从当前行开始，由于前边使用了next，此时从第二行循环)(此时是字符串列表)
    date.append(datetime.strptime(arrange[0],'%Y-%m-%d'))
    high.append(int(arrange[1]))
    low.append(int(arrange[3]))
#print(date,high,low)