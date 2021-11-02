import time
import requests
import json
from selenium import webdriver
import os
import pyautogui
from selenium.webdriver.common.by import By
import shutil

shutil.rmtree('D:/picture1/') 
os.mkdir('D:/picture1/')
#点击分享按钮
os.system("adb -s aeebf218 shell input tap 1005 170")
os.system("ping -n 2 127.0.0.1>nul")
#点击复制
os.system("adb -s aeebf218 shell input tap 352 1840")
os.system("ping -n 2 127.0.0.1>nul")
#打开浏览器
os.system("adb -s aeebf218 shell monkey -p com.vivo.browser -c android.intent.category.LAUNCHER 1")
os.system("ping -n 3 127.0.0.1>nul")
#刷新网页
os.system("adb -s aeebf218 shell input tap 951 164")
os.system("ping -n 2 127.0.0.1>nul")
#点击小红书分享地址
os.system("adb -s aeebf218 shell input swipe 740 760 740 760 1000")
os.system("ping -n 2 127.0.0.1>nul")
#点击粘贴按钮
os.system("adb -s aeebf218 shell input tap 106 632")
os.system("ping -n 2 127.0.0.1>nul")
#点击按钮
os.system("adb -s aeebf218 shell input tap 233 887")
os.system("ping -n 15 127.0.0.1>nul")

local = 'D:/picture1/'
pic = os.listdir(local)
for i in pic:
    os.system("adb -s aeebf218 push"+' '+local+i+' '+ "/sdcard/DCIM/Camera/")

os.system("adb -s aeebf218 shell am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d file:///sdcard/DCIM/Camera")   
#自动打开小红书
os.system("adb -s aeebf218 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
os.system("ping -n 5 127.0.0.1>nul")
#点返回
os.system("adb -s aeebf218 shell input tap 822 2286")
os.system("ping -n 2 127.0.0.1>nul")
#点击底部红色加号键
os.system("adb -s aeebf218 shell input tap 544 2168")
os.system("ping -n 2 127.0.0.1>nul")
#点返回
os.system("adb -s aeebf218 shell input tap 822 2286")
os.system("ping -n 2 127.0.0.1>nul")
#点击底部红色加号键
os.system("adb -s aeebf218 shell input tap 544 2168")
os.system("ping -n 2 127.0.0.1>nul")

print("选择图片")
img_add_num = 5
x_base = 298
x_add = 363
y_base = 435
y_add = 363
for i in range(0,img_add_num):
    x = x_base + x_add*(i%3)
    y = y_base + y_add*(int(i/3))
    os.system("adb -s aeebf218 shell input tap %s %s"%(x,y))
    time.sleep(0)
#点击下一步
os.system("adb -s aeebf218 shell input tap 929 2147")
os.system("ping -n 2 127.0.0.1>nul")  
#点击第二个下一步
os.system("adb -s aeebf218 shell input tap 982 171")
os.system("ping -n 2 127.0.0.1>nul")
#打开浏览器
os.system("adb -s aeebf218 shell monkey -p com.vivo.browser -c android.intent.category.LAUNCHER 1")
os.system("ping -n 3 127.0.0.1>nul")
#长按title
os.system("adb -s aeebf218 shell input swipe 770 1106 770 1106 1000")
os.system("ping -n 2 127.0.0.1>nul")
#扩选
os.system("adb -s aeebf218 shell input tap 350 964")
os.system("ping -n 2 127.0.0.1>nul")
#复制
os.system("adb -s aeebf218 shell input tap 372 957")
os.system("ping -n 2 127.0.0.1>nul")
#返回
os.system("adb -s aeebf218 shell input tap 834 2312")
os.system("ping -n 2 127.0.0.1>nul")
#点击desc
os.system("adb -s aeebf218 shell input tap 639 1348")
os.system("ping -n 2 127.0.0.1>nul")
#复制
os.system("adb -s aeebf218 shell input swipe 165 762 165 762 1000")
os.system("ping -n 2 127.0.0.1>nul")
#全选
os.system("adb -s aeebf218 shell input tap 72 636")
os.system("ping -n 2 127.0.0.1>nul")
#全选
os.system("adb -s aeebf218 shell input tap 138 623")
os.system("ping -n 2 127.0.0.1>nul")
#复制
os.system("adb -s aeebf218 shell input tap 264 580")
os.system("ping -n 2 127.0.0.1>nul")
#返回
os.system("adb -s aeebf218 shell input tap 834 2312")
os.system("ping -n 2 127.0.0.1>nul")
#自动打开小红书
os.system("adb -s aeebf218 shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1")
os.system("ping -n 5 127.0.0.1>nul")
#点击title位置
os.system("adb -s aeebf218 shell input swipe 502 692 502 692 500")
os.system("ping -n 2 127.0.0.1>nul")
#点击粘贴板
os.system("adb -s aeebf218 shell input tap 285 577")
os.system("ping -n 2 127.0.0.1>nul")
#点击第二个粘贴板title
os.system("adb -s aeebf218 shell input tap 534 1620")
os.system("ping -n 2 127.0.0.1>nul")
#点击desc位置
os.system("adb -s aeebf218 shell input tap 455 621")
os.system("ping -n 2 127.0.0.1>nul")
#点击desc的文本
os.system("adb -s aeebf218 shell input tap 202 1641")
os.system("ping -n 2 127.0.0.1>nul")
#关闭剪贴板
os.system("adb -s aeebf218 shell input tap 984 1431")
os.system("ping -n 2 127.0.0.1>nul")

