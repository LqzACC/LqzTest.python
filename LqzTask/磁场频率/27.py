import csv
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
config = {
    "font.family":'Times New Roman',  # 设置字体类型
    "font.size": 20,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

#写入输出地址
w=r'C:\Users\11389\Desktop\画图\磁场频率\27um\27um.csv'
o1=r'C:\Users\11389\Desktop\画图\磁场频率\27um\90_out.csv'
o2=r'C:\Users\11389\Desktop\画图\磁场频率\27um\9093_out.csv'
o3=r'C:\Users\11389\Desktop\画图\磁场频率\27um\93_out.csv'
o4=r'C:\Users\11389\Desktop\画图\磁场频率\27um\27um.png'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################

#补充点
ah,af=[],[]
for i in np.linspace(6,10,81):
    for n in range(150,300,1):
        ah=np.append(ah,i)
        af.append(n)

#原始计算数据写入
F,H,T=[],[],[]
for arrange in reader:
    try:
        h=float(arrange[0])
        f=float(arrange[1])
        t=float(arrange[2])
    except ValueError:
        print('not found data,please,check your code')
    else:
        F=np.append(F,f)
        H=np.append(H,h)
        T=np.append(T,t)

###############################################################90###############################################################
#数据分类(<90K)1
#挑拣出计算出的点
point_90_num,F_90,H_90,T_90=[],[],[],[]#分别是小于90K的对应点下标，倍数，频率，温度
i=0
for check_90 in T:
    if check_90 < float(90):
        f_90=F[i]
        h_90=H[i]
        t_90=T[i]
        F_90=np.append(F_90,f_90)
        H_90=np.append(H_90,h_90)
        T_90=np.append(T_90,t_90)
        point_90_num.append(i)
    i=i+1

i1=list(map(lambda x:x,point_90_num))
f1=list(map(lambda x:x,F_90))
h1=list(map(lambda x:x,H_90))
t1=list(map(lambda x:x,T_90))

outputpath=o1
outputfile=open(o1,'a+',newline='')
Writer = csv.writer(outputfile)
Writer.writerows(zip(f1,h1,t1,i1))

#上区间边缘
uhedge1,ufedge1=[],[]
for i in np.linspace(6.1,9.1,31):
    i=round(i, 1)#取小数点后一位
    indexe=H_90.tolist().index(i)
    uhedge1=np.append(uhedge1,H_90[indexe-1])
    ufedge1=np.append(ufedge1,F_90[indexe-1])
uhedge1=np.append(uhedge1,9.1)
ufedge1=np.append(ufedge1,150)
ufe1=list(map(lambda x:x,ufedge1))
uhe1=list(map(lambda x:x,uhedge1))

#上区间选点
u1n1,u1n2=[],[]
for i in range(len(ufe1)):
    for n in range(len(af)):
        if ufe1[i]-af[n]<=1 and ufe1[i]-af[n]>0 and uhe1[i]-ah[n]>0 and uhe1[i]-ah[n]<=0.1:
            u1n1.append(n)
        elif ufe1[i]-af[n]<=2 and ufe1[i]-af[n]>1 and uhe1[i]-ah[n]>0.1 and uhe1[i]-ah[n]<=0.2:
            u1n2.append(n)

for i in random.sample(u1n1,20):
    ufedge1=np.append(ufedge1,af[i])
    uhedge1=np.append(uhedge1,ah[i])
for i in random.sample(u1n2,10):
    ufedge1=np.append(ufedge1,af[i])
    uhedge1=np.append(uhedge1,ah[i])
uapp_ff1=list(map(lambda x:x,ufedge1))
uapp_hh1=list(map(lambda x:x,uhedge1))

###############################################################9093###############################################################
#数据分类(>90K&<93K)2
point_9093_num,F_9093,H_9093,T_9093=[],[],[],[]
i=0
for check_9093 in T:
    if check_9093 < float(93) and check_9093 >= float(90):
        f_9093=F[i]
        h_9093=H[i]
        t_9093=T[i]
        F_9093=np.append(F_9093,f_9093)
        H_9093=np.append(H_9093,h_9093)
        T_9093=np.append(T_9093,t_9093)
        point_9093_num.append(i)
    i=i+1

i2=list(map(lambda x:x,point_9093_num))
f2=list(map(lambda x:x,F_9093))
h2=list(map(lambda x:x,H_9093))
t2=list(map(lambda x:x,T_9093))

outputpath=o2
outputfile=open(o2,'a+',newline='')
Writer = csv.writer(outputfile)
Writer.writerows(zip(f2,h2,t2,i2))

#下区间边缘
dhedge,dfedge,dlinex,dliney=[],[],[],[]
for i in np.linspace(6,9.2,17):
    i=round(i, 1)#取小数点后一位
    indexe=H_9093.tolist().index(i)
    dhedge=np.append(dhedge,H_9093[indexe])
    dfedge=np.append(dfedge,F_9093[indexe])
    dlinex=np.append(dfedge,F_9093[indexe])
    dliney=np.append(dhedge,H_9093[indexe])
dfe2=list(map(lambda x:x,dfedge))
dhe2=list(map(lambda x:x,dhedge))

#下区间选点
d2n1,d2n2=[],[]
for i in range(len(dfe2)):
    for n in range(len(af)):
        if dfe2[i]-af[n]>=-1 and dfe2[i]-af[n]<0 and dhe2[i]-ah[n]<0 and dhe2[i]-ah[n]>=-0.1:
            d2n1.append(n)
        elif dfe2[i]-af[n]>=-2 and dfe2[i]-af[n]<-1 and dhe2[i]-ah[n]<-0.1 and dhe2[i]-ah[n]>=-0.2:
            d2n2.append(n)

dapp_f2,dapp_h2=[],[]
for i in random.sample(d2n1,20):
    dfedge=np.append(dfedge,af[i])
    dhedge=np.append(dhedge,ah[i])
for i in random.sample(d2n2,10):
    dfedge=np.append(dfedge,af[i])
    dhedge=np.append(dhedge,ah[i])
dapp_ff2=list(map(lambda x:x,dfedge))
dapp_hh2=list(map(lambda x:x,dhedge))


#上区间边缘
uhedge,ufedge,ulinex,uliney=[],[],[],[]
for i in np.linspace(6.1,9.9,39):
    i=round(i, 1)#取小数点后一位
    indexe=H_9093.tolist().index(i)
    uhedge=np.append(uhedge,H_9093[indexe-1])
    ufedge=np.append(ufedge,F_9093[indexe-1])
    ulinex=np.append(ufedge,F_9093[indexe-1])
    uliney=np.append(uhedge,H_9093[indexe-1])
uhedge=np.append(uhedge,9.9)
ufedge=np.append(ufedge,150)
ulinex=np.append(ufedge,150)
uliney=np.append(uhedge,9.9)
ufe2=list(map(lambda x:x,ufedge))
uhe2=list(map(lambda x:x,uhedge))

#上区间选点
u2n1,u2n2=[],[]
for i in range(len(ufe2)):
    for n in range(len(af)):
        if ufe2[i]-af[n]<=1 and ufe2[i]-af[n]>0 and uhe2[i]-ah[n]>0 and uhe2[i]-ah[n]<=0.1:
            u2n1.append(n)
        elif ufe2[i]-af[n]<=2 and ufe2[i]-af[n]>1 and uhe2[i]-ah[n]>0.1 and uhe2[i]-ah[n]<=0.2:
            u2n2.append(n)

uapp_f2,uapp_h2=[],[]
for i in random.sample(u2n1,20):
    ufedge=np.append(ufedge,af[i])
    uhedge=np.append(uhedge,ah[i])
for i in random.sample(u2n2,10):
    ufedge=np.append(ufedge,af[i])
    uhedge=np.append(uhedge,ah[i])
uapp_ff2=list(map(lambda x:x,ufedge))
uapp_hh2=list(map(lambda x:x,uhedge))

###############################################################93###############################################################
#数据分类(>93K)3
point_93_num,F_93,H_93,T_93=[],[],[],[]
i=0
for check_93 in T:
    if check_93 >= float(93):
        f_93=F[i]
        h_93=H[i]
        t_93=T[i]
        F_93=np.append(F_93,f_93)
        H_93=np.append(H_93,h_93)
        T_93=np.append(T_93,t_93)
        point_93_num.append(i)
    i=i+1

i3=list(map(lambda x:x,point_93_num))
f3=list(map(lambda x:x,F_93))
h3=list(map(lambda x:x,H_93))
t3=list(map(lambda x:x,T_93))

outputpath=o3
outputfile=open(o3,'a+',newline='')
Writer = csv.writer(outputfile)
Writer.writerows(zip(f3,h3,t3,i3))

#下区间边缘
dhedge3,dfedge3=[],[]
for i in np.linspace(6,10,21):
    i=round(i, 1)#取小数点后一位
    indexe=H_93.tolist().index(i)
    dhedge3=np.append(dhedge3,H_93[indexe])
    dfedge3=np.append(dfedge3,F_93[indexe])
dfe3=list(map(lambda x:x,dfedge3))
dhe3=list(map(lambda x:x,dhedge3))

#下区间选点
d3n1,d3n2=[],[]
for i in range(len(dfe3)):
    for n in range(len(af)):
        if dfe3[i]-af[n]>=-1 and dfe3[i]-af[n]<0 and dhe3[i]-ah[n]<0 and dhe3[i]-ah[n]>=-0.1:
            d3n1.append(n)
        elif dfe3[i]-af[n]>=-2 and dfe3[i]-af[n]<-1 and dhe3[i]-ah[n]<-0.1 and dhe3[i]-ah[n]>=-0.2:
            d3n2.append(n)

dapp_f2,dapp_h2=[],[]
for i in random.sample(d3n1,20):
    dfedge3=np.append(dfedge3,af[i])
    dhedge3=np.append(dhedge3,ah[i])
for i in random.sample(d3n2,10):
    dfedge3=np.append(dfedge3,af[i])
    dhedge3=np.append(dhedge3,ah[i])
dapp_ff3=list(map(lambda x:x,dfedge3))
dapp_hh3=list(map(lambda x:x,dhedge3))
###############################################################plot###############################################################
#绘图部分

font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
fig=plt.figure(dpi=100,figsize=(8,8))
ax=fig.add_subplot(111)#获取当前绘画区域
plt.rcParams['font.family']='Times New Roman'#设置字体
plt.rcParams['font.weight'] = 'normal'
plt.title('Cu 27um Thick B-f Curve')#标题
plt.style.use('ggplot')#背景色
plt.grid(linestyle='--',c='gray',zorder=10)#网格
plt.scatter(uapp_ff1,uapp_hh1,c='g',s=80,alpha=0.7,marker='^',linewidths=1,edgecolors='black')
plt.scatter(uapp_ff2+dapp_ff2,uapp_hh2+dapp_hh2,c='b',s=80,alpha=0.7,marker='^',linewidths=1,edgecolors='black')
plt.scatter(dapp_ff3,dapp_hh3,c='r',s=80,alpha=0.7,marker='^',linewidths=1,edgecolors='black')
#plt.scatter(f1,h1,c='r',s=80,alpha=0.7,marker='o',linewidths=1,edgecolors='black')
#plt.scatter(f2,h2,c='b',s=80,alpha=0.7,marker='o',linewidths=1,edgecolors='black')
#plt.scatter(f3,h3,c='g',s=80,alpha=0.7,marker='o',linewidths=1,edgecolors='black')
#plt.scatter(app_ff1,app_hh1,c='b',s=80,alpha=0.7,marker='o',linewidths=1,edgecolors='black')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')#文本
#plt.plot(dfe2,dfe2,label='test',color='red',linestyle=':',linewidth=1) 
plt.legend(['Superconductor','Thermal Balance','Thermal Runaway'],loc='upper right',prop=font1,frameon=True,edgecolor='black')#图注
plt.plot(dlinex.tolist(),dliney.tolist(),color='g',linestyle='-',linewidth=2)
plt.plot(ulinex.tolist(),uliney.tolist(),color='r',linestyle='-',linewidth=2) 
plt.xlabel("Frequency[Hz]",fontsize=22)
plt.ylabel("B[T]",fontsize=22,rotation='90')
plt.tick_params(axis='both',which='major',labelsize=14) #坐标轴
plt.axes().get_xaxis().set_visible(True)
plt.axes().get_yaxis().set_visible(True)
#plt.axis([48,202,0.78,1.22])#坐标范围
ax.set_xlim(145,305)
ax.set_ylim(5.8,10.2)
#ax2=ax.twinx()
y_major_locator=MultipleLocator(0.05)#刻度间距
x_major_locator=MultipleLocator(20)#刻度间距
ax.annotate('90K',xy=(190, 7.2), xycoords='data',fontsize=24,xytext=(170,6.4),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('93K',xy=(195, 7.6), xycoords='data',fontsize=24,xytext=(205,8.1),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'#坐标轴刻度向内
plt.savefig(o4)
plt.show()
