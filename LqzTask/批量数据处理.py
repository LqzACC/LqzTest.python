import csv
import numpy as np
from datetime import datetime

###############################################################CONST###############################################################
C=5e-6
m=0#Tem.index
###############################################################CONST###############################################################

#通项先行打开写入(减少迭代次数)
filepath=r'C:\Users\11389\Desktop\新建文件夹\新建文本文档.csv'
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)

#数据列头展示
for index,column_header in enumerate(head_row):
    print(index,column_header)

#通项写入
T,K=['T'],[]
for arrange in reader:
    try:
        t=float(arrange[0])
        k=float(arrange[1])*1e6
    except ValueError:
        print('not found data,please,check your code')
    else:
        T.append(t)
        K=np.append(K,k)
print(T,K)

#各组数据读取
for q in range(3,9,1):
    filepath=r'C:\Users\11389\Desktop\新建文件夹\%s.csv'%(q*100)
    file=open(filepath)
    reader=csv.reader(file)
    head_row=next(reader)

    #各组数据读入
    N,S,Sigmat=[],[],[]
    for arrange in reader:
        try:
            n=float(arrange[0])*1e20
            s=float(arrange[1])
            sigmat=float(arrange[2])/100
        except ValueError:
            print('not found data,please,check your code')
        else:
            N.append(n)
            S.append(s)
            Sigmat.append(sigmat)
    x=len(Sigmat)#判断数据集长度避免溢出或少计算
    #print(x)

    #输出列表初始化
    TAU=['tau']
    SIGMA=['sigma']
    ZT=['ZT']
    PF=['PF']
    ZT0=['ZT1']

    #输出计算
    for i in range(0,x,1):
        t=T[m+1]
        n=abs(N[i])

        tau=C*(1/t)*((1/n)**(1/3))
        TAU.append(tau)

        sigma=tau*Sigmat[i]
        SIGMA.append(sigma)

        zt=(t*(S[i]**(2))*sigma)/K[m]
        ZT.append(zt)

        pf=(S[i]**(2))*sigma*1e-6
        PF.append(pf)

        zt0=(t*pf)/K[m]
        ZT0.append(zt0)

    #一组输出
    N.insert(0,'n')
    #t=list(map(lambda x:x,T))
    n=list(map(lambda x:x,N))
    tau=list(map(lambda x:x,TAU))
    sigma=list(map(lambda x:x,SIGMA))
    zt=list(map(lambda x:x,ZT))
    pf=list(map(lambda x:x,PF))
    zt0=list(map(lambda x:x,ZT0))
    m=m+1

    outputpath=r'C:\Users\11389\Desktop\新建文件夹\out\%s.out.csv'%(q*100)
    outputfile=open(r'C:\Users\11389\Desktop\新建文件夹\out\%s.out.csv'%(q*100),'a+',newline='')
    Writer = csv.writer(outputfile)
    f=zip(n,tau,sigma,zt,pf,zt0)
    Writer.writerows(zip(n,tau,sigma,zt,pf,zt0))







