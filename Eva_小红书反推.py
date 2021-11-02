import time
import requests
import json
from selenium import webdriver
import os
import pyautogui
from selenium.webdriver.common.by import By
import shutil
def push():

    local = 'D:/picture1/'
    pic = os.listdir(local)
    print(pic)
    for i in pic:
        os.system("adb -s a333ba7a0321 push"+' '+local+i+' '+ "/sdcard/DCIM/Camera/")
def delte():
    dir = 'D:/picture1/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    print('used photos deleted!')


#点击分享按钮
os.system("adb -s a333ba7a0321 shell input tap 1000 166")
os.system("ping -n 2 127.0.0.1>nul")
#点击复制
os.system("adb -s a333ba7a0321 shell input tap 506 1893")
os.system("ping -n 2 127.0.0.1>nul")
#打开浏览器
os.system("adb -s a333ba7a0321 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
os.system("ping -n 3 127.0.0.1>nul")
#刷新网页
os.system("adb -s a333ba7a0321 shell input tap 964 164")
os.system("ping -n 2 127.0.0.1>nul")
#点击小红书分享地址
os.system("adb -s a333ba7a0321 shell input swipe 701 703 701 703 1000")
os.system("ping -n 2 127.0.0.1>nul")
#点击粘贴按钮
os.system("adb -s a333ba7a0321 shell input tap 141 568")
os.system("ping -n 2 127.0.0.1>nul")
#点击按钮
os.system("adb -s a333ba7a0321 shell input tap 235 806")
os.system("ping -n 25 127.0.0.1>nul")
print("----")

push()

os.system("adb -s a333ba7a0321 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera")
#自动打开小红书
os.system("adb -s a333ba7a0321 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
os.system("ping -n 5 127.0.0.1>nul")
#点返回
os.system("adb -s a333ba7a0321 shell input tap 790 2287")
os.system("ping -n 2 127.0.0.1>nul")
#点击底部红色加号键
os.system("adb -s a333ba7a0321 shell input tap 539 2175")
os.system("ping -n 2 127.0.0.1>nul")
#点返回
os.system("adb -s a333ba7a0321 shell input tap 790 2287")
os.system("ping -n 2 127.0.0.1>nul")
#点击底部红色加号键
os.system("adb -s a333ba7a0321 shell input tap 539 2175")
os.system("ping -n 2 127.0.0.1>nul")

print("选择图片")
img_add_num = 4
x_base = 304
x_add = 363
y_base = 412
y_add = 363
for i in range(0,img_add_num):
    x = x_base + x_add*(i%3)
    y = y_base + y_add*(int(i/3))
    os.system("adb -s a333ba7a0321 shell input tap %s %s"%(x,y))
    time.sleep(0)
#点击下一步
os.system("adb -s a333ba7a0321 shell input tap 929 2151")
os.system("ping -n 2 127.0.0.1>nul")  
#点击第二个下一步
os.system("adb -s a333ba7a0321 shell input tap 981 171")
os.system("ping -n 2 127.0.0.1>nul")
#打开浏览器
os.system("adb -s a333ba7a0321 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
os.system("ping -n 3 127.0.0.1>nul")
#长按title
os.system("adb -s a333ba7a0321 shell input swipe 195 1030 195 1030 1000")
os.system("ping -n 2 127.0.0.1>nul")
#扩选
os.system("adb -s a333ba7a0321 shell input tap 138 874")
os.system("ping -n 2 127.0.0.1>nul")
#复制
os.system("adb -s a333ba7a0321 shell input tap 483 850")
os.system("ping -n 2 127.0.0.1>nul")
#返回
os.system("adb -s a333ba7a0321 shell input tap 790 2287")
os.system("ping -n 2 127.0.0.1>nul")
#自动打开小红书
os.system("adb -s a333ba7a0321 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
os.system("ping -n 5 127.0.0.1>nul")
#点击title位置
os.system("adb -s a333ba7a0321 shell input swipe 203 622 203 622 1000")
os.system("ping -n 1 127.0.0.1>nul")
#粘贴
os.system("adb -s a333ba7a0321 shell input tap 81 519")
os.system("ping -n 1 127.0.0.1>nul")
#打开浏览器
os.system("adb -s a333ba7a0321 shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1")
os.system("ping -n 3 127.0.0.1>nul")
#点击desc
os.system("adb -s a333ba7a0321 shell input tap 201 1249")
os.system("ping -n 2 127.0.0.1>nul")
#复制
os.system("adb -s a333ba7a0321 shell input swipe 175 884 175 884 1000")
os.system("ping -n 2 127.0.0.1>nul")
#全选
os.system("adb -s a333ba7a0321 shell input tap 140 758")
os.system("ping -n 2 127.0.0.1>nul")
#复制
os.system("adb -s a333ba7a0321 shell input tap 480 698")
os.system("ping -n 2 127.0.0.1>nul")
#返回
os.system("adb -s a333ba7a0321 shell input tap 790 2287")
os.system("ping -n 2 127.0.0.1>nul")
#自动打开小红书
os.system("adb -s a333ba7a0321 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
os.system("ping -n 5 127.0.0.1>nul")

#点击desc位置
os.system("adb -s a333ba7a0321 shell input swipe 183 798 183 798 500")
os.system("ping -n 2 127.0.0.1>nul")
#粘贴
os.system("adb -s a333ba7a0321 shell input tap 87 607")
os.system("ping -n 2 127.0.0.1>nul")


delte()