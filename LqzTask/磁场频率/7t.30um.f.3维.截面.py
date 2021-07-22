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
    "font.size": 14,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

#写入输出地址
w=r'C:\Users\11389\Desktop\画图\磁场频率\30um\7t.csv'
o1=r'C:\Users\11389\Desktop\画图\磁场频率\30um\7t.png'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
W,T1,T2,T3,T4,T5,T6,T7,T8,T9=[],[],[],[],[],[],[],[],[],[]
for arrange in reader:
    try:
        w=float(arrange[0])
        t1=float(arrange[1])
        t2=float(arrange[2])
        t3=float(arrange[3])
        t4=float(arrange[4])
        t5=float(arrange[5])
        t6=float(arrange[6])
        t7=float(arrange[7])
        t8=float(arrange[8])
        t9=float(arrange[9])
    except ValueError:
        print('not found data,please,check your code')
    else:
        W=np.append(W,w)
        T1=np.append(T1,t1)
        T2=np.append(T2,t2)
        T3=np.append(T3,t3)
        T4=np.append(T4,t4)
        T5=np.append(T5,t5)
        T6=np.append(T6,t6)
        T7=np.append(T7,t7)
        T8=np.append(T8,t8)
        T9=np.append(T9,t9)
Tc=[]
Tc.append(T1)
Tc.append(T2)
Tc.append(T3)
Tc.append(T4)
Tc.append(T5)
Tc.append(T6)
Tc.append(T7)
Tc.append(T8)
Tc.append(T9)

F=[]
for i in range(180,223,5):
    F.append(i)
###############################################################core###############################################################

ax = plt.figure().add_subplot(projection='3d')
verts = []
x=np.linspace(0., 4., 401)
y=F

n=0
for i in y:#频率
    z = Tc[n].tolist()#温度
    verts.append([(x[0], 85), *zip(x, z), (x[-1], 85)])
    n=n+1

poly = PolyCollection(verts, facecolors=['mediumspringgreen', 'darkgreen', 
                                         'plum', 'darkviolet', 'mediumpurple', 'indigo',
                                         'pink','lightcoral', 'red'], alpha=0.7)
ax.add_collection3d(poly, zs=y, zdir='y')

ax.set_xlabel('Width[mm]',fontsize=16)
ax.set_ylabel('Frequency[Hz]',fontsize=16)
ax.set_zlabel('Temperature[K]',fontsize=16)
ax.set_xlim(0, 4)
ax.set_ylim(178,222)
ax.set_zlim(85, 165)
#ax.set_xticks([0, 0.5,1,1.5, 2,2.5, 3,3.5,4])
#ax.set_zticks([85, 90, 100,110,120,130,140,150,160,165])
#ax.set_yticks([180, 185, 190,195,200,205,210,215,220])
ax.tick_params(axis='y', rotation=0)
ax.set_title('0.2s 30um Thick 7T Vary Frequency')
plt.savefig(o1)
plt.show()

