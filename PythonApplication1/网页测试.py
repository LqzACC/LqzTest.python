from selenium import webdriver
brower=webdriver.Chrome()
brower.get('https://www.gamersky.com/ent/201710/966689_48.shtml')
link=brower.find_element_by_link_text('首页')
type(link)
link.click()
#brower.quit()
#import openpyxl
#A=openpyxl.load_workbook('C:\\Users\\Lqz\\source\\repos\\PythonApplication1\\PythonApplication1\\ss.xlsx')
#type(A)
#print(A.get_sheet_names())time.sleep(10)