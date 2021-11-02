import pyautogui

def move_and_click(x,y,sleeptime):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    pyautogui.sleep(sleeptime)
def move_and_click_write(x,y,sleeptime,input_str,press):
    pyautogui.moveTo(x=x,y=y,duration=0,tween=pyautogui.linear)
    pyautogui.click(x=x,y=y,clicks=1,button='left')
    pyautogui.sleep(sleeptime)
    pyautogui.typewrite(input_str)
    pyautogui.press(press)   
def move_and_click_right(x,y,sleeptime):
    pyautogui.moveTo(x=x,y=y,duration=0,tween=pyautogui.linear)
    pyautogui.click(x=x,y=y,clicks=1,button='right')
    pyautogui.sleep(sleeptime)
def move_and_click_paste(x,y,sleeptime):
    pyautogui.moveTo(x=x,y=y,duration=0,tween=pyautogui.linear)
    pyautogui.click(x=x,y=y,clicks=1,button='left')
    pyautogui.hotkey("ctrl", "v")
    pyautogui.sleep(sleeptime)

num = 1
end_num = 40
a=0
for i in range(num,end_num):
    move_and_click(1144,252,2)
    move_and_click(1144,252,0)
    #rem("输入文本")
    js_str="document.getElementsByTagName('p')[%s].textContent"%(a)
    move_and_click_write(1144,280,1,js_str,'enter')
    #rem("点击视频链接")
    move_and_click(1343,325,1)
    #rem("右击视频")
    move_and_click_right(731,534,2)
    #rem("点击复制视频地址")
    move_and_click(828,688,2)
    #rem("消除弹出的页面")
    move_and_click(589,20,2)
    #rem("点击pyautogui")
    move_and_click(605,1052,2)
    #rem("放入链接")
    move_and_click_paste(342,237,2)
    #rem("保存")
    pyautogui.hotkey("ctrl","s")
    #rem("点击命令列表")
    move_and_click(666,1054,2)
    #rem("点击命令界面")
    move_and_click(786,955,2)
    #rem("输入get_xhs_video.py")
    pyautogui.typewrite("get_xhs_videos.py")
    pyautogui.press("enter")
    #rem("点击pyautogui")
    move_and_click(605,1052,2)
    pyautogui.hotkey("ctrl","z")
    #rem("返回chorme")
    move_and_click(539,1053,2)
    a +=1






