import csv
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
from matplotlib.image import NonUniformImage
from matplotlib import cm

config = {
    "font.family":'Times New Roman',  # 设置字体类型
    "font.size": 20,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

#写入输出地址
w=r'C:\Users\11389\Desktop\画图\交流频率\20um\t-1.02Ic.190hz.csv'
o1=r'C:\Users\11389\Desktop\画图\交流频率\20um\t-1.02Ic.190hz.png'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
T1,Te1,T2,Te2,T3,Te3,T4,Te4=[],[],[],[],[],[],[],[]
for arrange in reader:
    try:
        t1=float(arrange[0])
        te1=float(arrange[1])
        t2=float(arrange[2])
        te2=float(arrange[3])
        t3=float(arrange[4])
        te3=float(arrange[5])
        t4=float(arrange[6])
        te4=float(arrange[7])
    except ValueError:
        print('not found data,please,check your code')
    else:
        T1=np.append(T1,t1)
        Te1=np.append(Te1,te1)
        T2=np.append(T2,t2)
        Te2=np.append(Te2,te2)
        T3=np.append(T3,t3)
        Te3=np.append(Te3,te3)
        T4=np.append(T4,t4)
        Te4=np.append(Te4,te4)

font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}
fig=plt.figure(dpi=100,figsize=(8,8))
ax=fig.add_subplot(111)#获取当前绘画区域
plt.rcParams['font.family']='Times New Roman'#设置字体
plt.rcParams['font.weight'] = 'normal'
plt.title('1.02Ic Vary F Time-K')#标题
plt.style.use('ggplot')#背景色
plt.grid(linestyle='--',c='gray',zorder=10)#网格

plt.plot(T4.tolist(),Te4.tolist(),c='gray',linestyle='-',linewidth=2,label='200Hz')
plt.plot(T3.tolist(),Te3.tolist(),c='b',linestyle='-',linewidth=2,label='150Hz')
plt.plot(T2.tolist(),Te2.tolist(),c='g',linestyle='-',linewidth=2,label='100Hz')
plt.plot(T1.tolist(),Te1.tolist(),c='r',linestyle='-',linewidth=2,label='50Hz')

plt.legend(loc='lower right',prop=font1,frameon=True,edgecolor='black')#图注
plt.xlabel("Time[s]",fontsize=22)
plt.ylabel("T[K]",fontsize=22,rotation='90')
plt.tick_params(axis='both',which='major',labelsize=14) #坐标轴
plt.axes().get_xaxis().set_visible(True)
plt.axes().get_yaxis().set_visible(True)
ax.set_xlim(0,0.5)
ax.set_ylim(77,93)
#ax2=ax.twinx()
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'#坐标轴刻度向内
plt.savefig(o1)
plt.show()
