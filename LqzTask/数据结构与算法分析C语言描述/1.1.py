1.1
#Q1一个有N个数的列表，选出其中第K个最大值。
#random.random()随即生成[0,1)之间的浮点数
#random.randint(a,b)生成[a,b]范围内的整数
#random.randrange(a,b,step)生成[a,b)范围内的整数
#random.uniform(a,b)生成[a,b]范围内的随机浮点数
#random.choice(seq)从非空序列中选出一个数据带回
#random.choices(seq,weights=None,*,cum_weights=None,k=1)seq数据集,weights相对权重,cum_weights累加权重,k选取次数(放回)
#random.sample(seq,k)k选取个数(不放回)
#random.shuffle(seq)打乱分布重新排列，无返回值
#random.seed(a=None,version=2)设置种子
"""
import random
N=[]
for n in range(100):
    N.append(n)
k=5
#A1:降序排列，选出第K个元素。
random.shuffle(N)
for i in range(0,100):
    for n in range(i+1,100):
        if N[i]<N[n]:
            m=N[i]
            N[i]=N[n]
            N[n]=m
print(N[k])
#A2:取前K个插入，排序，后续与第K个比较，若大写入再排序，弱小则忽略
random.shuffle(N)
B=[]
for i in range(0,k):
    B.append(N[i])
for i in range(0,k):
    for n in range(i+1,k):
        if B[i]<B[n]:
            m=B[i]
            B[i]=B[n]
            B[n]=m
for m in range(k,100):
    if N[m]>B[k-1]:
        B[k-1]=N[m]
    for i in range(0,k):
        for n in range(i+1,k):
            if B[i]<B[n]:
                m=B[i]
                B[i]=B[n]
                B[n]=m
print(B)
"""

#Q2矩阵字母表查找单词
#list与array互换np.array(list),.tolist()
#.reshape(d1,d2,d3,d4...)或.shape=(d1,d2,d3...)仅支持转换数组型为矩阵
#.ndim秩.size矩阵元素个数.shape每一秩元素个数
#coefficients系数矩阵,dependents因变量矩阵,解矩阵np.linalg.solve(coefficients,dependents),np.dot(coefficients,dependents)矩阵点积
"""
import numpy as np
a='thiswatsoahgfgdt'
b=[]
for i in range(0,16):
    b.append(a[i])
b=np.array(b)
b=b.reshape(4,4)
print(b)
Dwords=[]
#横向
rwords=[]
for r in range(0,4):
    for c in range(0,4):
        o=b[r][c]
        rwords.append(o)
        for n in range(c+1,4):
            o=o+b[r][n]
            rwords.append(o)
print(rwords)
#纵向加对角
cwords=[]
for c in range(0,4):
    for r in range(0,4):
        j=c
        o=b[r][c]
        o2=o
        cwords.append(o)
        Dwords.append(o2) 
        for n in range(r+1,4):
            o=o+b[n][c]
            cwords.append(o)
            j=j+1
            if j<=3:
                o2=o2+b[n][j]
                Dwords.append(o2)
print(cwords)
print(Dwords)
wordslist=cwords+Dwords+rwords
words=['this','two','fat','that']
for i in range(4):
    if words[i] in wordslist:
        print(words[i])
"""