import pyautogui
import time
#鼠标移动到chrome 
pyautogui.moveTo(x=544, y=1062,duration=0, tween=pyautogui.linear)
pyautogui.click(x=544, y=1062,clicks=1, button='right')
time.sleep(2)
pyautogui.moveTo(x=600, y=920,duration=0, tween=pyautogui.linear)
pyautogui.click(x=600, y=920,clicks=1, button='left')
time.sleep(2)
pyautogui.moveTo(x=196, y=64,duration=0, tween=pyautogui.linear)
pyautogui.click(x=196, y=64,clicks=1, button='left')
pyautogui.typewrite("http://www.baidu.com")
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(x=583, y=1048,duration=0, tween=pyautogui.linear)
pyautogui.click(x=583, y=1048,clicks=1, button='left')
time.sleep(1)
pyautogui.moveTo(x=1750, y=82,duration=0, tween=pyautogui.linear)
pyautogui.click(x=1750, y=82,clicks=1, button='left')
time.sleep(1)
pyautogui.moveTo(x=1452, y=111,duration=0, tween=pyautogui.linear)
pyautogui.click(x=1452, y=111,clicks=1, button='left')
pyautogui.click(x=1452, y=111,clicks=1, button='left')
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.moveTo(x=630, y=392,duration=0, tween=pyautogui.linear)
pyautogui.click(x=630, y=392,clicks=1, button='left')
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('enter')