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
w=r'C:\Users\11389\Desktop\画图\磁场角度\7t.0-90d.vf.csv'
o1=r'C:\Users\11389\Desktop\画图\磁场角度\W1.7t.0-90d.vf.png'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
Degree,W,F180,F190,F200,F210,F220=[],[],[],[],[],[],[]
for arrange in reader:
    try:
        de=float(arrange[0])
        w=float(arrange[1])
    except ValueError:
        print('not found data,please,check your code')
    else:
        Degree=np.append(Degree,de)
        W=np.append(W,w)

Theta=[]
for i in range(0,7):
    Theta=np.append(Theta,Degree[i])
    F180=np.append(F180,W[i])
    F190=np.append(F190,W[i+7])
    F200=np.append(F200,W[i+14])
    F210=np.append(F210,W[i+21])
    F220=np.append(F220,W[i+28])
print(Theta)

font1 = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16,
}#图例参数

fig=plt.figure(dpi=100,figsize=(8,8))
ax=fig.add_subplot(111)#获取当前绘画区域
#ax.set_yscale("log")
plt.rcParams['font.family']='Times New Roman'#设置字体
plt.rcParams['font.weight'] = 'normal'
plt.title('0.2s Cu 30um Thick All layer')#标题
plt.style.use('ggplot')#背景色
plt.grid(linestyle='--',c='gray',zorder=10)#网格

plt.plot(Theta.tolist(),F220.tolist(),c='plum',linestyle='-',linewidth=2,label='220Hz')
plt.plot(Theta.tolist(),F220.tolist(), 'v',c='plum',markerfacecolor='white',markeredgecolor='plum');

plt.plot(Theta.tolist(),F210.tolist(),c='gray',linestyle='-',linewidth=2,label='210Hz')
plt.plot(Theta.tolist(),F210.tolist(), '^',c='gray',markerfacecolor='white',markeredgecolor='gray');

plt.plot(Theta.tolist(),F200.tolist(),c='b',linestyle='-',linewidth=2,label='200Hz')
plt.plot(Theta.tolist(),F200.tolist(), 'd',c='b',markerfacecolor='white',markeredgecolor='b');

plt.plot(Theta.tolist(),F190.tolist(),c='g',linestyle='-',linewidth=2,label='190Hz')
plt.plot(Theta.tolist(),F190.tolist(), 's',c='g',markerfacecolor='white',markeredgecolor='g');

plt.plot(Theta.tolist(),F180.tolist(),c='r',linestyle='-',linewidth=2,label='180Hz')
plt.plot(Theta.tolist(),F180.tolist(), 'o',c='r',markerfacecolor='white',markeredgecolor='r');

plt.legend(loc='upper right',prop=font1,frameon=True,edgecolor='black')#图注facecolor添加背景色
plt.xlabel('Degree'+'['+r'$\theta_{}$'+']',fontsize=22)
plt.ylabel("AC Loss[W/m]",fontsize=22,rotation='90')
plt.tick_params(axis='both',which='major',labelsize=16) #坐标轴
plt.axes().get_xaxis().set_visible(True)
plt.axes().get_yaxis().set_visible(True)
ax.set_xlim(-2,92)#轴范围
ax.set_ylim(1200,3800)#轴范围
plt.xticks(Theta.tolist())#轴刻度
#plt.yticks(range(80,200,20))#轴刻度
#ax2=ax.twinx()#双轴
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'#坐标轴刻度向内
plt.savefig(o1)
plt.show()