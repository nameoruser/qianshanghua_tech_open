import pyautogui
import time
num=1
#刷新第一页
#清除blogger/v2
pyautogui.moveTo(x=1419, y=211,duration=0, tween=pyautogui.linear)
pyautogui.click(x=1419, y=211,clicks=1, button='left')
pyautogui.sleep(2)
#清除response
pyautogui.moveTo(x=1496, y=178,duration=0, tween=pyautogui.linear)
pyautogui.click(x=1496, y=178,clicks=1, button='left')
pyautogui.sleep(2)
#点击console
pyautogui.moveTo(x=1430, y=145,duration=0, tween=pyautogui.linear)
pyautogui.click(x=1430, y=145,clicks=1, button='left')
pyautogui.sleep(2)

pyautogui.moveTo(x=1260, y=207,duration=0, tween=pyautogui.linear)
pyautogui.click(x=1260, y=207,clicks=1, button='left')
pyautogui.typewrite('$(".corona-pagination_pagination").children[1].click()')
pyautogui.press('enter')
pyautogui.sleep(1)
#清除console
for i in range(num,46):
    print("执行第%s页"%(i))
    pyautogui.moveTo(x=1267, y=177,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1267, y=177,clicks=1, button='left')
    pyautogui.sleep(5)
    #跳转到network
    pyautogui.moveTo(x=1585, y=147,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1585, y=147,clicks=1, button='left')
    pyautogui.sleep(1)
    #移动到fetch
    pyautogui.moveTo(x=1513, y=275,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1513, y=275,clicks=1, button='left')
    pyautogui.sleep(1)
    #enter blogger/v2
    pyautogui.moveTo(x=1360, y=210,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1360, y=210,clicks=1, button='left')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite("blogger/v2")
    pyautogui.press('enter')
    pyautogui.sleep(3)
    #点击 blogger/v2
    pyautogui.moveTo(x=1360, y=295,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1360, y=295,clicks=1, button='left')
    pyautogui.sleep(1)
    #点击response
    pyautogui.moveTo(x=1727, y=437,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1727, y=437,clicks=1, button='left')
    pyautogui.sleep(1)
    #移动到data,并点击，复制
    pyautogui.moveTo(x=1669, y=470,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1669, y=470,clicks=1, button='left')
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    pyautogui.sleep(1)
    #移除response
    pyautogui.moveTo(x=1494, y=178,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1494, y=178,clicks=1, button='left')
    pyautogui.sleep(1)
    #点击粘贴界面
    pyautogui.moveTo(x=730, y=20,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=730, y=20,clicks=1, button='left')
    pyautogui.sleep(1)
    #找到粘贴地方，并粘贴
    pyautogui.moveTo(x=1083, y=214,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1083, y=214,clicks=1, button='left')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.sleep(1)
    #点击提交
    pyautogui.moveTo(x=1119, y=320,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1119, y=320,clicks=1, button='left')
    pyautogui.sleep(1)
    #点击回原小红书
    pyautogui.moveTo(x=150, y=20,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=150, y=20,clicks=1, button='left')
    pyautogui.sleep(1)
    #点击console,并跳转下一页
    pyautogui.moveTo(x=1428, y=146,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=1428, y=146,clicks=1, button='left')
    pyautogui.typewrite('$(".corona-pagination_pagination").children[$(".corona-pagination_pagination").children.length-1].click()')
    pyautogui.press('enter')
    pyautogui.sleep(1)

