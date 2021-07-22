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

#文件读取
filepath=r'C:\Users\11389\Desktop\画图\交流频率\20um\20um.csv'
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
#原始计算数据写入
F,P,T=[],[],[]
u90,d90,u95,d95=[1.0,1.005,1.01,1.015,1.02],[1.03,1.035,1.04,1.045,1.05],[1.16,1.165,1.17,1.175,1.18],[1.19,1.195,1.2,1.205,1.21]#20
for arrange in reader:
    try:
        p=float(arrange[0])
        f=float(arrange[1])
        t=float(arrange[2])
    except ValueError:
        print('not found data,please,check your code')
    else:
        F=np.append(F,f)
        P=np.append(P,p)
        T=np.append(T,t)

#数据分类(<90K)
#挑拣出计算出的点
point_90_num,F_90,P_90,T_90=[],[],[],[]#分别是小于90K的对应点下标，倍数，频率，温度
i=0
for check_90 in T:
    if check_90 < float(90):
        f_90=F[i]
        p_90=P[i]
        t_90=T[i]
        F_90=np.append(F_90,f_90)
        P_90=np.append(P_90,p_90)
        T_90=np.append(T_90,t_90)
        point_90_num.append(i)
    i=i+1

#print(len(F_90))=128
F_90s,P_90s=[],[]
n=1
for i in random.sample(range(0,len(F_90),1),30):
    F_90s=np.append(F_90s,F_90[i])
    P_90s=np.append(P_90s,P_90[i])

#补充填点
app_f1,app_p1=[],[]
n=1
for t in u90:
    for i in random.sample(range(51,200,1),10*n):
        app_f1.append(i)
        app_p1.append(t)
    n=n+1

for i in range(0,len(F_90s)):
    app_f1.append(F_90s[i])
    app_p1.append(P_90s[i])


i1=list(map(lambda x:x,point_90_num))
f1=list(map(lambda x:x,F_90))
p1=list(map(lambda x:x,P_90))
t1=list(map(lambda x:x,T_90))
app_ff1=list(map(lambda x:x,app_f1))
app_pp1=list(map(lambda x:x,app_p1))

outputpath=r'C:\Users\11389\Desktop\画图\交流频率\20um\90_out.csv'
outputfile=open(r'C:\Users\11389\Desktop\画图\交流频率\20um\90_out.csv','a+',newline='')
Writer = csv.writer(outputfile)
Writer.writerows(zip(f1,p1,t1))
Writer.writerows(zip(app_ff1,app_pp1))

#数据分类(>90K&<95K)
point_9095_num,F_9095,P_9095,T_9095=[],[],[],[]
i=0
for check_9095 in T:
    if check_9095 < float(95) and check_9095 >= float(90):
        f_9095=F[i]
        p_9095=P[i]
        t_9095=T[i]
        F_9095=np.append(F_9095,f_9095)
        P_9095=np.append(P_9095,p_9095)
        T_9095=np.append(T_9095,t_9095)
        point_9095_num.append(i)
    i=i+1

#print(len(F_9095))=128
F_9095s,P_9095s=[],[]
n=1
for i in random.sample(range(0,len(F_9095),1),30):
    F_9095s=np.append(F_9095s,F_9095[i])
    P_9095s=np.append(P_9095s,P_9095[i])

#补充填点
app_f2,app_p2=[],[]
n=5
for t in d90:
    for i in random.sample(range(51,200,1),10*n):
        app_f2.append(i)
        app_p2.append(t)
    n=n-1

n=1
for t in u95:
    for i in random.sample(range(51,200,1),10*n):
        app_f2.append(i)
        app_p2.append(t)
    n=n+1

for i in range(0,len(F_9095s)):
    app_f2.append(F_9095s[i])
    app_p2.append(P_9095s[i])

i2=list(map(lambda x:x,point_9095_num))
f2=list(map(lambda x:x,F_9095))
p2=list(map(lambda x:x,P_9095))
t2=list(map(lambda x:x,T_9095))
app_ff2=list(map(lambda x:x,app_f2))
app_pp2=list(map(lambda x:x,app_p2))

outputpath=r'C:\Users\11389\Desktop\画图\交流频率\20um\9095_out.csv'
outputfile=open(r'C:\Users\11389\Desktop\画图\交流频率\20um\9095_out.csv','a+',newline='')
Writer = csv.writer(outputfile)
Writer.writerows(zip(f2,p2,t2))
Writer.writerows(zip(app_ff2,app_pp2))

#数据分类(>95K)
point_95_num,F_95,P_95,T_95=[],[],[],[]
i=0
for check_95 in T:
    if check_95 >= float(95):
        f_95=F[i]
        p_95=P[i]
        t_95=T[i]
        F_95=np.append(F_95,f_95)
        P_95=np.append(P_95,p_95)
        T_95=np.append(T_95,t_95)
        point_95_num.append(i)
    i=i+1

#print(len(F_95))=80
F_95s,P_95s=[],[]
n=1
for i in random.sample(range(0,len(F_95),1),40):
    F_95s=np.append(F_95s,F_95[i])
    P_95s=np.append(P_95s,P_95[i])

#补充填点
app_f3,app_p3=[],[]
n=5
for t in d95:
    for i in random.sample(range(51,200,1),10*n):
        app_f3.append(i)
        app_p3.append(t)
    n=n-1

for i in range(0,len(F_95s)):
    app_f3.append(F_95s[i])
    app_p3.append(P_95s[i])

i3=list(map(lambda x:x,point_95_num))
f3=list(map(lambda x:x,F_95))
p3=list(map(lambda x:x,P_95))
t3=list(map(lambda x:x,T_95))
app_ff3=list(map(lambda x:x,app_f3))
app_pp3=list(map(lambda x:x,app_p3))

outputpath=r'C:\Users\11389\Desktop\画图\交流频率\20um\95_out.csv'
outputfile=open(r'C:\Users\11389\Desktop\画图\交流频率\20um\95_out.csv','a+',newline='')
Writer = csv.writer(outputfile)
Writer.writerows(zip(f3,p3,t3))
Writer.writerows(zip(app_ff3,app_pp3))

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
plt.title('Cu 20um Thick I0-f Curve')#标题
plt.style.use('ggplot')#背景色
plt.grid(linestyle='--',c='gray',zorder=10)#网格
plt.scatter(app_ff1,app_pp1,c='g',s=80,alpha=0.7,marker='D',linewidths=1,edgecolors='black')
plt.scatter(app_ff2,app_pp2,c='b',s=80,alpha=0.7,marker='D',linewidths=1,edgecolors='black')
plt.scatter(app_ff3,app_pp3,c='r',s=80,alpha=0.7,marker='D',linewidths=1,edgecolors='black')
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')#文本
plt.legend(['Superconductor','Thermal Balance','Thermal runaway'],loc='lower right',prop=font1,frameon=True,edgecolor='black')#图注
plt.xlabel("Frequency[Hz]",fontsize=22)
plt.ylabel("I0/Ic[A]",fontsize=22,rotation='90')
plt.tick_params(axis='both',which='major',labelsize=14) #坐标轴
plt.axes().get_xaxis().set_visible(True)
plt.axes().get_yaxis().set_visible(True)
#plt.axis([48,202,0.78,1.22])#坐标范围
ax.set_xlim(45,205)
ax.set_ylim(0.78,1.32)
#ax2=ax.twinx()
y_major_locator=MultipleLocator(0.05)#刻度间距
x_major_locator=MultipleLocator(20)#刻度间距
ax.axhline(1.185, linestyle='-',c='r')
ax.axhline(1.025, linestyle='-',c='g')#水平虚线
ax.annotate('84.11K',xy=(205, 0.795), xycoords='data',fontsize=14)
ax.annotate('86.10K',xy=(205, 0.895), xycoords='data',fontsize=14)
ax.annotate('88.70K',xy=(205, 0.995), xycoords='data',fontsize=14)
ax.annotate('91.37K',xy=(205, 1.095), xycoords='data',fontsize=14)
ax.annotate('315.16K',xy=(205, 1.195), xycoords='data',fontsize=14)
ax.annotate('433.63K',xy=(205, 1.295), xycoords='data',fontsize=14)
ax.annotate('90K',xy=(80, 1.02), xycoords='data',fontsize=24,xytext=(60,1.08),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('95K',xy=(80, 1.19), xycoords='data',fontsize=24,xytext=(60,1.11),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'#坐标轴刻度向内
plt.savefig(r'C:\Users\11389\Desktop\画图\交流频率\20um\20um.png')
plt.show()







  