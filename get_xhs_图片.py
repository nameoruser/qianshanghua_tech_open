import requests
import time
import json
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

# url_now = "https://www.qianshanghua.com/api/page/comment/load?chat_id=8e940b2524c843789d29278c8d2b8cdc&comment_id="
# a = requests.get(url_now)
# a = a.text
# b = json.loads(a)
driver_pages = []
url_list = ["http://xhslink.com/K2zmwe"]
# for comment in b["comments"]:
#     c = comment[4]
#     if "http://" in c:
#         d= "http://"+c.split("，")[1].split("http://")[1]
#         url_list.append(d)
#         print(d)
driver = webdriver.Chrome()
def get_picture(picture_url):
    aim_url = picture_url
    print("download:", aim_url)
    aim_response = requests.get(aim_url)
    t = int(round(time.time() * 1000))  # 毫秒集
    f = open(os.path.join(os.path.dirname(__file__), 'D:/picture1/%s.%s' % (time.time(), "jpg")), "ab")
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
    try:
        e = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/div[1]/div[1]/div[1]/ul")
        h1 = e.find_elements(By.TAG_NAME, "li")
        for h in h1:
            style = h.find_element(By.CLASS_NAME, "inner")
            picture = style.get_attribute("style")
            tu = "http:" + picture.split('("')[1]
            get_picture(tu)
    except:
        print("笔记消失")

driver.close()