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
w=r'C:\Users\11389\Desktop\画图\磁场角度\6-10.0-90.200hz.csv'
o1=r'C:\Users\11389\Desktop\画图\磁场角度\6-10.0-90.200hz.png'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
Degree,T,B6,B7,B8,B9,B10=[],[],[],[],[],[],[]
for arrange in reader:
    try:
        de=float(arrange[1])
        t=float(arrange[2])
    except ValueError:
        print('not found data,please,check your code')
    else:
        Degree=np.append(Degree,de)
        T=np.append(T,t)

Theta=[]
for i in range(0,7):
    Theta=np.append(Theta,Degree[i])
    B6=np.append(B6,T[i])
    B7=np.append(B7,T[i+7])
    B8=np.append(B8,T[i+14])
    B9=np.append(B9,T[i+21])
    B10=np.append(B10,T[i+28])
print(Theta)

font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}#图例参数
fig=plt.figure(dpi=100,figsize=(8,8))
ax=fig.add_subplot(111)#获取当前绘画区域
plt.rcParams['font.family']='Times New Roman'#设置字体
plt.rcParams['font.weight'] = 'normal'
plt.title('0.2s Cu 30um Thick')#标题
plt.style.use('ggplot')#背景色
plt.grid(linestyle='--',c='gray',zorder=10)#网格

plt.plot(Theta.tolist(),B10.tolist(),c='plum',linestyle='-',linewidth=2,label='10T')
plt.plot(Theta.tolist(),B10.tolist(), 'v',c='plum',markerfacecolor='white',markeredgecolor='plum');

plt.plot(Theta.tolist(),B9.tolist(),c='gray',linestyle='-',linewidth=2,label='9T')
plt.plot(Theta.tolist(),B9.tolist(), '^',c='gray',markerfacecolor='white',markeredgecolor='gray');

plt.plot(Theta.tolist(),B8.tolist(),c='b',linestyle='-',linewidth=2,label='8T')
plt.plot(Theta.tolist(),B8.tolist(), 'd',c='b',markerfacecolor='white',markeredgecolor='b');

plt.plot(Theta.tolist(),B7.tolist(),c='g',linestyle='-',linewidth=2,label='7T')
plt.plot(Theta.tolist(),B7.tolist(), 's',c='g',markerfacecolor='white',markeredgecolor='g');

plt.plot(Theta.tolist(),B6.tolist(),c='r',linestyle='-',linewidth=2,label='6T')
plt.plot(Theta.tolist(),B6.tolist(), 'o',c='r',markerfacecolor='white',markeredgecolor='r');

plt.legend(loc='upper right',prop=font1,frameon=True,edgecolor='black')#图注facecolor添加背景色
plt.xlabel('Degree'+'['+r'$\theta_{}$'+']',fontsize=22)
plt.ylabel("Temperature[K]",fontsize=22,rotation='90')
plt.tick_params(axis='both',which='major',labelsize=16) #坐标轴
plt.axes().get_xaxis().set_visible(True)
plt.axes().get_yaxis().set_visible(True)
ax.set_xlim(-2,92)#轴范围
ax.set_ylim(85,500)#轴范围
plt.xticks(Theta.tolist())#轴刻度
#plt.yticks(range(80,200,20))#轴刻度
#ax2=ax.twinx()#双轴
y_major_locator=MultipleLocator(5)#刻度间距
x_major_locator=MultipleLocator(0.02)#刻度间距
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'#坐标轴刻度向内
plt.savefig(o1)
plt.show()