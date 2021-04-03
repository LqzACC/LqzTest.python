import webbrowser,requests,bs4,sys,os,threading
from selenium import webdriver
#考虑学习CSS,Javascript

#网页打开
"""
webbrowser.open('https://www.zhihu.com/follow')
"""

#网页下载
"""
res=requests.get('https://www.zhihu.com/follow')
res.status_code=requests.codes.ok
try:
    res.raise_for_status()
except BaseException as err:
    print('can not download')
else:
    print('yes it work')

file=open('webdownload.txt','wb')
for text in res:
    file.write(text)
file.close()
#将下载的网页写入本地.txt文件中
"""

#打开指定网址的几页
"""
res=requests.get('https://tieba.baidu.com/f?kw=%CF%D4%BF%A8&fr=ala0&tpl=5')
res.status_code=requests.codes.ok
try:
    res.raise_for_status()
except BaseException as err:
    print('can not work')
else:
    print('work successful')

file=open('link.txt','wb')
for text in res:
    file.write(text)
file.close()

example=bs4.BeautifulSoup(res.text,features="lxml")
#打开非本地链接，用.text,理解为直接对原网页操作
elm=example.select('.j_th_tit a')#('.Class X')在X中寻找有Class的
#.j_th_tit类型为class,在<a>中筛选具有j_th_tit属性的Class,其中.不能丢，网页中显示为class="j_th_tit "
numOpen=min(5,len(elm))
for i in range(numOpen):
    print(elm[i].getText())
    webbrowser.open('https://tieba.baidu.com'+elm[i].get('href'))
"""

"""
file=open('test.html')
example=bs4.BeautifulSoup(file.read(),features="lxml")
elm=example.select('span')#[0]
#返回一个网页的Tag对象列表
print(len(elm[0]))
print(elm[0].getText())
#返回该标签<>....</>中对应的文本
print(str(elm[0]))
#返回<>....</>
print(elm[0].attrs)
#以字典形式输出属性
#打开本地存储的网页,用.read()
"""

#自动批量从网页下载(单线程)
"""
#自动批量从网页下载(单线程)
url='https://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    xkcd=requests.get(url)
    xkcd.status_code==requests.codes.ok
    try:
        xkcd.raise_for_status()
    except BaseException as err:
        print('not work')

    example=bs4.BeautifulSoup(xkcd.text,features='lxml')
    exkcd=example.select('#comic img')#('#属性 X')在属性中寻找有X的

    if exkcd==[]:
        print('not found')
    else:
        xkcdurl='http:'+exkcd[0].get('src')
        res=requests.get(xkcdurl)
        res.status_code==requests.codes.ok
        imagefile=open(os.path.join('xkcd',os.path.basename(xkcdurl)),'wb')
        for text in res:
            imagefile.write(text)
    prelink=example.select('a[rel="prev"]')[0]
    url='https://xkcd.com'+prelink.get('href')

        #select返回的对像中get函数，括号里为属性
"""

#自动批量从网页下载(多线程)
"""
os.makedirs('download',exist_ok=True)
def download(startpage,endpage):#多线程
    for numpage in range(startpage,endpage):
        print('current download page is %s'%(numpage))
        url='https://xkcd.com/%s/'%(numpage)
        xkcd=requests.get(url)
        xkcd.status_code==requests.codes.ok
        try:
            xkcd.raise_for_status()
        except BaseException as err:
            print('not work')

        example=bs4.BeautifulSoup(xkcd.text,features='lxml')
        imag=example.select('#comic img')
        if imag==[]:
            print('not found')
        else:
            imgurl='http:'+imag[0].get('src')
            try:
                res=requests.get(imgurl)
            except BaseException as err:
                print('%s not exist'%(imgurl))
            else:
                res.status_code==requests.codes.ok
            file=open(os.path.join('download',os.path.basename(imgurl)),'wb')
            for a in res:
                file.write(a)
            file.close()

for i in range(1,2000,10):
    downloadTask = threading.Thread(target=download, args=(i,i+9))
    downloadTask.start()
"""

#填充网页,需要学习javascript
"""
brower=webdriver.Chrome()
brower.get('https://gmis.shu.edu.cn/shuweb/index.html#/login?redirect=%2Ffunc%2Fnewdoc%2FGRXXXG%2FGNEW%2F20720115')
link=brower.find_element_by_class_name('el-button el-button--success el-button--medium')
link.click()
user_code=brower.find_element_by_id('username')
user_code.send_keys('20720115')
user_pass=brower.find_element_by_id('password')
user_pass.send_keys('Lqz1138951849')
user_sub=brower.find_element_by_id('submit')
user_sub.click()
#brower.quit()
#import openpyxl
#A=openpyxl.load_workbook('C:\\Users\\Lqz\\source\\repos\\PythonApplication1\\PythonApplication1\\ss.xlsx')
#type(A)
#print(A.get_sheet_names())time.sleep(10)
"""