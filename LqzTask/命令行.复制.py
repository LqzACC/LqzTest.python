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

#1.在命令行中执行.py程序，将存储.py文件添加入全局变量，win+r 输入cmd → xxx.py+xxxxx
#2.利用.bat批处理，自动执行.py程序，
#@echo off 
#start cmd /k xxxx.py+xxx
#$pip install --.whl
#$pip -r requirements.txt
#matplotlib
#pygame
#requests
#pip
