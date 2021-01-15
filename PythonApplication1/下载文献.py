import webbrowser,requests,bs4,sys,os,threading,time
from selenium import webdriver

def downloadessay():
    """
    #SUST
    url1='https://iopscience.iop.org/'
    open1=webdriver.Chrome()
    open1.get(url1)
    link=open1.find_element_by_class_name('nav-top-link-drop-down.nav-item nav-search.active')
    link.click()
    search=open1.find_element_by_id('quickSearch')
    search.send_keys(keywords)
    link2=cdown.find_element_by_class_name('btn.btn-default.hdr-search-btn.bd-0.art-lookup__submit')
    link2.click()
    """

    #get essay url
    url2='https://iopscience.iop.org/nsearch?terms='+'superconductor+FEM+Electromagnetic'
    open2=requests.get(url2)
    open2.status_code==requests.codes.ok
    try:
        open2.raise_for_status
    except BaseException as err:
        print('ERROR')
    else:
        print('success!')
    essayhtml=bs4.BeautifulSoup(open2.text,features='lxml')
    essaypage=essayhtml.select('.art-list-item-title')
    if essaypage==[]:
        print('not found')
    else:
        durl='https://iopscience.iop.org'+essaypage[0].get('href')
        print(durl)

    """
    #SCI-HUB
    url3='https://sci-hub.se/'
    open3=webdriver.Chrome()
    open3.get(url3)
    search2=open3.find_element_by_id('sci-hub-plugin-check')
    search.send_keys(durl)
    link3=open3.find_element_by_class_name('')
    link3.click()
    """

downloadessay()

"""
i='y'
N=1
keys=[]
while i=='y':
    i=input('是否输入关键词，按下y or n:')
    try:
        if i=='y':
            key=input('请输入第'+str(N)+'个关键词:')
            keys.append(key)
            N=N+1
        else:
            #print('关键词输入完毕，请稍后。')
            keyword=''
            for a in range(1,len(keys)):
                keyword=keyword+'+'+keys[a]
                keywords=keys[0]+keyword
            print(keywords)
            downloadessay(keywords)

    except BaseException as err:
        print('没有输入关键词。')
"""





