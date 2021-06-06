import csv
from datetime import datetime
import numpy as np

###############################################################CONST###############################################################
C=5e-6
l=1
###############################################################CONST###############################################################

#通项先行打开写入(减少迭代次数)
filepath=r'C:\Users\11389\Desktop\新建文件夹\新建文本文档.csv'
file=open(filepath)
reader=csv.reader(file)
head_row=next(reader)
K,T=[],['T']
for arrange in reader:
    t=float(arrange[0])
    k=float(arrange[16])
    T.append(t)
    K=np.append(K,k)

#各组数据读取
for i in range(1,14,3):
    filepath=r'C:\Users\11389\Desktop\新建文件夹\新建文本文档.csv'
    file=open(filepath)
    reader=csv.reader(file)
    head_row=next(reader)

    N,S,Sigmat=[],[],[]
    for arrange in reader:
        try:
            n=float(arrange[i])
            s=float(arrange[i+1])
            sigmat=float(arrange[i+2])/100
        except ValueError:
            print('not found data,please,check your code')
        else:
            N.append(n)
            S.append(s)
            Sigmat.append(sigmat)

    #result var
    TAU=['tau%s'%(l)]
    SIGMA=['sigma%s'%(l)]
    ZT=['ZT%s'%(l)]
    PF=['PF%s'%(l)]
    ZT0=['ZT1%s'%(l)]
    l=l+1

    #参数计算
    for m in range(0,5):
        t=T[m+1]
        n=N[m]

        tau=C*(1/t)*((1/n)**(1/3))
        TAU.append(tau)

        sigma=tau*Sigmat[m]
        SIGMA.append(sigma)

        zt=(t*(S[m]**(2))*sigma)/K[m]
        ZT.append(zt)

        pf=(S[m]**(2))*sigma*1e-6
        PF.append(pf)

        zt0=(t*pf)/K[m]
        ZT0.append(zt0)

    #一组输出
    N.insert(0,'n%s'%(l))
    t=list(map(lambda x:x,T))
    n=list(map(lambda x:x,N))
    tau=list(map(lambda x:x,TAU))
    sigma=list(map(lambda x:x,SIGMA))
    zt=list(map(lambda x:x,ZT))
    pf=list(map(lambda x:x,PF))
    zt0=list(map(lambda x:x,ZT0))

    outputpath=r'C:\Users\11389\Desktop\新建文件夹\out.csv'
    outputfile=open(r'C:\Users\11389\Desktop\新建文件夹\out.csv','a+',newline='')
    Writer = csv.writer(outputfile)
    f=zip(t,n,tau,sigma,zt,pf,zt0)
    Writer.writerows(zip(t,n,tau,sigma,zt,pf,zt0))