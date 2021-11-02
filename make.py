#850.4  721.6
import pyautogui
def move_and_click(x,y,sleeptime):
    pyautogui.moveTo(x=x, y=y,duration=0, tween=pyautogui.linear)
    pyautogui.click(x=x, y=y,clicks=1, button='left')
    pyautogui.sleep(sleeptime)

num = 1
urls=[] 

for i in range (1,10):
    for url in urls:
        move_and_click(336,17,2)
        move_and_click(402,67,2)
        pyautogui.press("enter")
    pyautogui.hotkey("ctrl","shift","i")
    move_and_click(1274,216,2)
    move_and_click(1118,252,2)
    move_and_click(1249,280,2)
    pyautogui.typewrite("$('video').src")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    move_and_click(1690,306,0)
    move_and_click(1690,306,0)
    move_and_click(1690,306,0)
    pyautogui.hotkey("ctrl","c")
    pyautogui.sleep(1)
    move_and_click(607,1052,2)
    pyautogui.sleep(1)
    move_and_click(509,133,2)
    pyautogui.hotkey("ctrl","v")
    pyautogui.hotkey("ctrl","s")
    move_and_click(668,1050,2)
    pyautogui.sleep(1)
    move_and_click(769,934,2)
    pyautogui.sleep(1)
    pyautogui.typewrite("get_auto.py")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(1)
    # 点击回pyautogui撤回网址
    move_and_click(607,1052,2)
    pyautogui.hotkey("ctrl","z")
    move_and_click(544,1052,2)
    move_and_click(588,18,2)
    move_and_click(148,18,2)

