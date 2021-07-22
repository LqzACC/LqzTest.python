import csv
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
from matplotlib.image import NonUniformImage
from matplotlib import cm

#写入输出地址
w=r'C:\Users\11389\Desktop\画图\磁场频率\30um\2d_screen.csv'
o1=r'C:\Users\11389\Desktop\画图\磁场频率\30um\2d_screen.csv'

#文件读取
filepath=w
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

###############################################################core###############################################################
# setup some generic data
X,Y,T=[],[],[]
for arrange in reader:
    try:
        x=float(arrange[0])
        y=float(arrange[1])
        t=float(arrange[2])
    except ValueError:
        print('not found data,please,check your code')
    else:
        X=np.append(X,x)
        Y=np.append(Y,y)
        T=np.append(T,t)
#print(len(Y))

Z,Z1=[],[]
for i in range(0,401,401):
    for n in range(i,i+401):
        Z1=np.append(Z1,T[n])
    Z.append(Z1.tolist())

interp = 'nearest'

# Linear x array for cell centers:
x = np.linspace(0, 4, 401)
# Highly nonlinear x array:
y = np.linspace(0, 0.113,11)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
print(z)
fig, axs = plt.subplots(nrows=1, ncols=1, constrained_layout=True)
fig.suptitle('NonUniformImage class', fontsize='large')
ax = axs
im = NonUniformImage(ax, interpolation=interp, extent=(0,  4, 0, 0.113),
                     cmap=cm.Purples)
im.set_data(x, y, z)
ax.add_image(im)
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 0.12)
ax.set_title(interp)
plt.show()

