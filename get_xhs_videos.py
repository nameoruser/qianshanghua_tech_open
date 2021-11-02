import time
import requests
import json
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

url_now = "https://www.qianshanghua.com/api/page/comment/load?chat_id=9724fbedab6843fb934e67b618474b2d&comment_id="
a = requests.get(url_now)
a = a.text
b = json.loads(a)
url_list = []
driver_pages = []
for comment in b["comments"]:
    c = comment[4]
    if "http://" in c:
        d="http://"+c.split("，")[1].split("http://")[1]
        url_list.append(d)
driver = webdriver.Chrome()
def get_video(video_url):
    aim_url = video_url
    print("download:", aim_url)
    aim_response = requests.get(aim_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__), 'D:/video/%s.%s' % (time.time(), "mp4")), "ab")
    f.write(aim_response.content)
    f.close()
for u in url_list:
    driver.get(u)
    time.sleep(4)
    current_url = driver.current_url
    current_url = current_url.split("?")[0]
    if current_url in driver_pages:
        continue
    driver_pages.append(current_url)
    src = driver.find_element(By.TAG_NAME, "video")
    video = src.get_attribute("src")
    get_video(video)
driver.close()

