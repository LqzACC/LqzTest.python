import csv
from datetime import datetime
import matplotlib.pyplot as plt

a,b={},{}
for i in range(1,5):
    filepath=r'C:\Users\lqz\Desktop\新建文件夹\%s.csv'%(i)
    file=open(filepath)
    reader=csv.reader(file)
    head_row=next(reader)
    a[i]=[]
    b[i]=[]
    for index,column_header in enumerate(head_row):
        print(index,column_header)
    for arrange in reader:
        try:
            x=float(arrange[0])
            y=float(arrange[1])+float(2000*(i-1))
        except ValueError:
            print('not found data,please,check your code')
        else:
            a[i].append(x)
            b[i].append(y)
    #print(a[i],b[i])

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(a[1],b[1],color='red',alpha=0.5)
plt.plot(a[2],b[2],color='blue',alpha=0.5)
plt.plot(a[3],b[3],color='green',alpha=0.5)
plt.plot(a[4],b[4],color='purple',alpha=0.5)
#plt.fill_between(CSV文件操作.date, CSV文件操作.high, CSV文件操作.low, facecolor='blue', alpha=0.1)
plt.title('XRD',fontsize=24)
plt.xlabel('2θ/deg',fontsize=16)
#fig.autofmt_xdate()
plt.ylabel('Intensity',fontsize=16)
plt.tick_params(axis='both',width=2,labelsize=10) 
plt.tick_params(direction='in',width=2,length=4)
plt.yticks([])
plt.savefig(r'C:\Users\lqz\Desktop\新建文件夹\XRD.png')
plt.show()