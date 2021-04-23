#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.
import webbrowser,sys,pyperclip
if len(sys.argv) > 1:
 # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
 # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
print(address)
# TODO: Get address from clipboard.

#配置环境变量3个
#:\Users\11389\AppData\Roaming\Python\Python37\Scripts
#:\Microsoft SDK\Microsoft Visual Studio\Shared\Python37_64\python.exe
#:\Microsoft SDK\Microsoft Visual Studio\Shared\Python37_64\Scripts

#1.在命令行中执行.py程序，将存储.py文件添加入全局变量，win+r 输入cmd → xxx.py+xxxxx
#2.利用.bat批处理，自动执行.py程序，
#@echo off 
#start cmd /k xxxx.py+xxx

#$py -m pip --version 先检查pip版本 
#$pip install --upgrade pip pip版本升级

#$pip install --.whl 有时候安装失败，考虑是网络的问题
#$pip -r requirements.txt
#matplotlib,pygame,requests,scipy,send2trash,beautifulsoup4,selenium,openpyxl,PyPDF2,python-docx,imapclient,pyzmail,twilio,pillow,pyautogui,pip,numpy+mkl
#pyobjc-core（仅在 OS X 上）,pyobjc（仅在 OS X 上）,python3-xlib（仅在 Linux 上）

#git还原:将某一次更改全部撤回并新建一次更改。重置-hard:在某一次提交上进行重置，本地代码将回滚到该次提交，且删除之后的提交。重置-mixed:在某一次提交上进行重置，本地代码回滚到该次提交。
#git挑拣:将某一次的提交并入当前提交中，A-B-C-D，对A进行挑拣，将A中不同的代码合并入D中。