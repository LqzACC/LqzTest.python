import pyautogui
#pyautogui.PAUSE = 1
#pyautogui.FAILSAFE = True
#pyautogui.position()#获取当前位置
#pyautogui.click（100，150，button='left'）#在座标处点击鼠标左键
#pyautogui.doubleClick()#双击左键
#pyautogui.rightClick()#双击右键
#pyautogui.middleClick()#双击中建
#pyautogui.dragTo()#同时按住一个键拖动
#pyautogui.dragRel()#同时按住一个键拖动
#pyautogui.scroll(200)#向上或向下滚动
#pyautogui.screenshot()#截图
#.pixelMatchesColor(x,y,(r,g,b))#坐标颜色匹配函数
#.locateOnScreen('filename')#匹配区域屏幕快照的坐标，4整数元组，(左顶x,左顶y,长，宽)
#pyautogui.center((左顶x,左顶y,长，宽))#获取该区域中心点坐标
#pyautogui.typewrite(['str'])#可选列表型参数，对按键的调用
#pyautogui.keyDown()/.press()/.keyUp()
#pyautogui.hotkey('shift','4')#热键组合


"""
for i in range(10):#从起始坐标处开始移动
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
"""
"""
for i in range(10):#从当前鼠标位置开始移动
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
"""
"""
print('Press Ctrl-C to quit.') 
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)#.rjust()右对齐
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except BaseException as err:
    print('\nDone.')
"""
"""
im = pyautogui.screenshot()
im.getpixel((50, 200))
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
"""


