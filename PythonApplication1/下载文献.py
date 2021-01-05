import webbrowser,requests,bs4,sys,os,threading,time
from selenium import webdriver

def downloadessay(keywords):

    url='https://iopscience.iop.org/'
    cdown=webdriver.Chrome()
    cdown.get(url)
    time.sleep(60)
    link=cdown.find_element_by_class_name('nav-top-link-drop-down nav-item nav-search active')
    link.click()
    search=cdown.find_element_by_id('quickSearch')
    search.send_keys(keywords)
    link2=cdown.find_element_by_class_name('btn btn-default hdr-search-btn bd-0 art-lookup__submit')
    link2.click()

    url2='https://iopscience.iop.org/nsearch?terms='+'keywords'
    down=requests.get(url2)
    down.status_code==requests.codes.ok
    try:
        down.raise_for_status
    except BaseException as err:
        print('ERROR')
    else:
        print('success!')
    essay=bs4.BeautifulSoup(down.text,features='lxml')
    downessay=essay.select('href')

downloadessay()

