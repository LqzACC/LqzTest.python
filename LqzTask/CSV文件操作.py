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

"""
#写入
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')
#delimiter选择替换逗号的符号,lineterminator选择行间隔
#readerObj.line_num确定行号
outputFile.close()
data.to_csv('splitData\wodecesi.csv',index = False)
Writer = csv.writer(outputfile)
Writer.writerows(map(lambda x: [x], List))
#可直接竖向排列
"""

#inputpath=r'C:\Users\lqz\Desktop\新建文件夹\77.5K Angle Dependence.csv'
outputpath=r'C:\Users\lqz\Desktop\新建文件夹\output.csv'
#inputfile=open(inputpath)
outputfile=open(r'C:\Users\lqz\Desktop\新建文件夹\output1.csv','w',newline='')
#reader=csv.reader(inputfile)
#head_row=next(reader)
#(next(reader)返回一个全局变量)

#for index,column_header in enumerate(head_row):
    #print(index,column_header)
"""
#w：以写方式打开， 
#a：以追加模式打开 (从 EOF 开始, 必要时创建新文件) 
#r+：以读写模式打开 
#w+：以读写模式打开 (参见 w ) 
#a+：以读写模式打开 (参见 a ) 
#rb：以二进制读模式打开 
#wb：以二进制写模式打开 (参见 w ) 
#ab：以二进制追加模式打开 (参见 a ) 
#rb+：以二进制读写模式打开 (参见 r+ ) 
#wb+：以二进制读写模式打开 (参见 w+ ) 
#ab+：以二进制读写模式打开 (参见 a+ )
"""

Current,d=[],[]
"""
for column in reader:
        CriticalCurrent=float(column[3])
        if reader.line_num > 716:
            Current.append(str(CriticalCurrent))
"""
c=30
for i in range(0,601):
    Current.append(i)
for i in np.arange(0,30.1,0.1):#range()只能处理整数，np.arange()可以处理浮点数
    d.append(i)
for i in range(1,301):
    d.append(c)

Writer = csv.writer(outputfile)
a=list(map(lambda x:x,Current))
b=list(map(lambda x:x,d))
c=zip(a,b)
print(list(c))
Writer.writerows(zip(a,b))

#writerows()必须是可迭代的，eg:元组列表
#list(zip(a,b))==[(),(),()....]or[[],[],[]....]

#lambda x:x+1  返回计算结果  f(x)=y=x+1 e.g.f=lambda x:x+1 f(3)=4
#map(function,iterable)  返回迭代器对象 e.g. <map object at 0x7fc638814c10> 
#map+lambda   map(lambda x:x+1,list)
#filter() e.g.  filter(function,list) list中带入function，返回true的数取出来做成列表