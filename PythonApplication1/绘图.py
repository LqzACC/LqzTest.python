#URL='https://matplotlib.org/index.html'图表

import matplotlib.pyplot as plt
import numpy as np
import pygal,matplotlib,json,pygal_maps_world
import CSV文件操作,JSON文件操作
from JSON文件操作 import world_population,w_p1,w_p2,w_p3
from datetime import datetime
from random_walk import RandomWalk,Die
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from pygal.style import RotateStyle,LightColorizedStyle

"""
#plot 曲线图(指定→函数模拟)
x=list(range(1,100))
y=[v**2 for v in x]
plt.plot(x,y,label='test',color='red',linestyle=':',linewidth=1) 
    #(x输入列表，y输出列表，线标签，颜色，线风格，线宽)
plt.legend(loc='upper left')
    #(标签位置)
plt.title("square",fontsize=24)
    #(文本大小用FONTSIZE)
plt.xlabel("x",fontsize=14)
plt.ylabel("y",fontsize=14)
plt.tick_params(axis='both',labelsize=14) 
    #(刻度)
plt.show()
"""

"""
#scatter 散点图(单次模拟→函数模拟→随机数模拟→多次随机模拟)
x=list(range(1,100)) or x=[1,2,3]
y=[f(x)] or y=[1,2,3]
for v in x:
    v=v*v
    y.append(v)
"""
"""
while True:
    N=input('你想模拟多少个点？请输入。\nN=')
    rw=RandomWalk(int(N))
    rw.fill_walk()
    plt.figure(dpi=80,figsize=(10,6))
    num_point=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=num_point,cmap=plt.cm.Blues,s=14)
        #(点大小用s)(color(R,G,B)颜色参数 0~1,语句用c，单个推荐用color)(edgecolor='none'去除点轮廓)(c=,cmap=*.cm.Blues颜色映射根据y值)
        #(URL='https://matplotlib.org/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py'cmap颜色参考)
    plt.title("square",fontsize=24) 
        #(文本大小用FONTSIZE)
    plt.xlabel("N",fontsize=14)
    plt.ylabel("square",fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=14) 
        #(刻度)
    plt.scatter(rw.x_values[0],rw.y_values[0],color='black',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],color='red',s=100)
        #(挑出某个点，注意绘制顺序)Z
    #plt.axes().get_xaxis().set_visible(True)
    #plt.axes().get_yaxis().set_visible(True)
        #(xy轴是否可见)
    #plt.axis([1,1000,1,1000])#坐标范围
        #(该项可选，若不选，则系统默认)
    plt.show()
    #plt.savefig('D:\\scatter.jpg',bbox_inches='tight')
        #(该项可选，若不选，则系统默认)
    keep_running=input('你想继续吗?请按下y OR n\n')
    if keep_running == 'n':
        break
    #(savefig('文件名实参,默认位置，可选绝对路径'，'是否保留空白实参'))
"""

"""
#柱状图pygal实现(掷色子1次→2次叠加)
die1=Die(6)
die2=Die(10)
N=input('你想模拟多少次？输入\nN=')
num,NUM,Frequency,labels=[],[],[],[]
NUM1,NUM2,NUM3,NUM4,NUM5,NUM6=0,0,0,0,0,0
for roll_nums in range(int(N)):
    side=die1.roll()+die2.roll()
    num.append(side)
    print(num)
        #(两种统计方式第一种可优化)
for i in num:
    if i==1:
        NUM1=NUM1+1
    elif i==2:
        NUM2=NUM2+1
    elif i==3:
        NUM3=NUM3+1
    elif i==4:
        NUM4=NUM4+1
    elif i==5:
        NUM5=NUM5+1
    elif i==6:
        NUM6=NUM6+1
NUM.extend([NUM1,NUM2,NUM3,NUM4,NUM5,NUM6])
max_sides=die1.num_sides+die2.num_sides
for i in range(2,max_sides+1):
    frequency=num.count(i)
    Frequency.append(frequency)  
    labels.append(str(i))
print(Frequency)
        #(两种统计方式第一种可优化)
hist=pygal.Bar()
hist.title='Frequency of Die'
hist.x_labels=labels
hist.x_title='result'
hist.y_title='frequency'
hist.add('D6+D6',Frequency)
hist.render_to_file('D:\\Bar.svg')
"""

"""
#柱状图matplotlib实现
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    #Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
"""

"""
#图表
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(CSV文件操作.date,CSV文件操作.high,color='red',alpha=0.5)
plt.plot(CSV文件操作.date,CSV文件操作.low,color='blue',alpha=0.5)
plt.fill_between(CSV文件操作.date, CSV文件操作.high, CSV文件操作.low, facecolor='blue', alpha=0.1)
plt.title('tempature',fontsize=24)
plt.xlabel('DATE',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('tempature',fontsize=16)
plt.tick_params(axis='both',labelsize=10) 
plt.show()
"""

"""
#3D图
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
X = np.linspace(-1, 1, 4)
Y = np.linspace(-2, 2, 5)
print(np.shape(X))
print(np.shape(Y))
print(X)
print(Y)
X, Y = np.meshgrid(X, Y)
print(np.shape(X))
print(np.shape(Y))
print(X)
print(Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
Z=X*0+4
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
plt.show()
"""

"""
#散点分布图
np.random.seed(19680801)
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')
ax.legend()
ax.grid(True)
plt.show()
"""

"""
#南丁格尔玫瑰图
import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

month = ['一月','二月','三月','四月','五月','六月',
         '七月','八月','九月','十月','十一月','十二月']
cost = [827.4,827.4,827.4,827.4,827.4,827.4,3051.1,4946.5,3326.3,2823.4,4589.1,2347.4]
color_series = ['#C9DA36','#9ECB3C','#6DBC49',
                '#3DBA78','#14ADCF','#209AC9',
                '#2C6BA0','#2D3D8E','#6A368B'
                '#7D3990','#A63F98','#C31C88',]

df = pd.DataFrame({'month': month, 'cost': cost})
print(df)
d=df.sort_values(by='cost', ascending=False, inplace=True)
#ascending升序排列，inplace置换,true替换df永久的,False不替换原来的仅返回排序后的
print(d)
print(df)

a = df['month'].values.tolist()
b = df['cost'].values.tolist()
print(a)
print(b)

pie1 = Pie(init_opts=opts.InitOpts(width='900px', height='750px'))
pie1.set_colors(color_series)
# 添加数据，设置饼图的半径，是否展示成南丁格尔图
pie1.add("", [list(z) for z in zip(a, b)],
        radius=["20%", "115%"],
        center=["50%", "65%"],
        rosetype="area"
        )
# 设置全局配置项
pie1.set_global_opts(title_opts=opts.TitleOpts(title='2021年度财报'),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())
# 设置系列配置项
pie1.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12,
                                               formatter="{b}:{c}元", font_style="italic",
                                               font_weight="bold", font_family="Microsoft YaHei"
                                               ),
                     )
pie1.render('绘图.html')
"""

#"""
#世界地图
wm_style=pygal.style.RotateStyle('#3399AA')
wm=pygal.maps.world.World(style=wm_style)
wm = pygal_maps_world.maps.World()
wm.title = 'world population distribution'
wm.add('0-10Million',w_p1)
wm.add('10-1000Million',w_p2)
wm.add('>10Billion',w_p3)
wm.render_to_file('world_population.svg') 
#"""
