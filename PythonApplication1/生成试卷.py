import random,os
province={'hn':'zz','bj':'bj','sd':'qd','zj':'hz','js':'nj','sh':'sh','gd':'gz','fj':'fz','gx':'nn','sx':'xa'}
#os.makedirs('F:\\代码')
for testnum in range(7):         #创建试卷
    #os.makedirs('E:\\code\\test%s.txt'%(testnum+1))
    file_test=open('F:\\代码\\test%s.txt'%(testnum+1),'w')
    file_test_a=open('F:\\代码\\test_a%s.txt'%(testnum+1),'w')
    file_test.write('Name:\n\nDate:\n\nperiod:\n\n')
    file_test.write((' '*20)+'state quiz (from %s)'%(testnum+1)+'\n\n')
    A=list(province.keys())       #province 键列表
    random.shuffle(A)             #A键列表打乱顺序重排列
    for i in range(10):
        correction_a=province[A[i]]
        incorrection_a=list(province.values())
        del incorrection_a[incorrection_a.index(correction_a)]
        incorrection_a=random.sample(incorrection_a,3)
        a_Options=incorrection_a+[correction_a]
        random.shuffle(a_Options)
        dot=['A','B','C','D']

        file_test.write('%s.which one is %s city.\n'%(i+1,A[i]))
        for n in range(4):
            file_test.write('%s.%s\n'%(dot[n],a_Options[n]))
        file_test.write('\n')

        #file_test_a.write(' '*20+'%s answer\n'%(testnum+1))
        file_test_a.write('%s.%s\n'%(i+1,dot[a_Options.index(correction_a)]))
        file_test_a.write('\n')
file_test.close()
file_test_a.close()