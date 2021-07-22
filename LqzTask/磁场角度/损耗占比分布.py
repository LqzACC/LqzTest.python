from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import csv
import random
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
config = {
    "font.family":'Times New Roman',  # 设置字体类型
    "font.size": 22,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

#写入输出地址
w=r'C:\Users\11389\Desktop\画图\磁场角度\7t.210hz.90d.csv'
o1=r'C:\Users\11389\Desktop\画图\磁场角度\7t.210hz.90d.png'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
Time,W,W1=[],[],[]
for arrange in reader:
    try:
        t=float(arrange[0])
        w=float(arrange[1])
        w1=float(arrange[2])-w
    except ValueError:
        print('not found data,please,check your code')
    else:
        Time=np.append(Time,t)
        W=np.append(W,w)
        W1=np.append(W1,w1)

font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}#图例参数
fig=plt.figure(dpi=100,figsize=(8,8))
ax=fig.add_subplot(111)#获取当前绘画区域
ax.set_yscale("log")
plt.rcParams['font.family']='Times New Roman'#设置字体
plt.rcParams['font.weight'] = 'normal'
plt.title('7t 210Hz')#标题
plt.style.use('ggplot')#背景色
plt.grid(linestyle='--',c='gray',zorder=10)#网格
plt.plot(Time.tolist(),W.tolist(),c='salmon',linestyle='-',linewidth=2,label='Superconductor layer', alpha=1)
plt.plot(Time.tolist(),W1.tolist(),c='lightskyblue',linestyle='-',linewidth=2,label='All layer', alpha=0.6)
#ax.fill_between(Time.tolist(), W.tolist(), 0, facecolor='black', alpha=1)
#ax.fill_between(Time.tolist(), W1.tolist(), 0, facecolor='lightskyblue', alpha=0.3)
plt.legend(loc='upper left',prop=font1,frameon=True,edgecolor='black')#图注facecolor添加背景色
plt.xlabel('Time[s]',fontsize=22)
plt.ylabel("AC Loss[W/m]",fontsize=22,rotation='90')
plt.tick_params(axis='both',which='major',labelsize=16) #坐标轴
plt.axes().get_xaxis().set_visible(True)
plt.axes().get_yaxis().set_visible(True)
ax.set_xlim(0,0.202)#轴范围
ax.set_ylim(0,1e6)#轴范围
#plt.xticks(Time.tolist())#轴刻度
#plt.yticks(range(80,200,20))#轴刻度
#ax2=ax.twinx()#双轴
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'#坐标轴刻度向内
plt.savefig(o1)
plt.show()