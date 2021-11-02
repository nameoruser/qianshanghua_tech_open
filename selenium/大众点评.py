from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import json
import time

driver = webdriver.Chrome()
e = driver.find_elements(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[1]/div[2]/ul")
print(e)
#//*[@id="shop-all-list"]/ul/li[15]/div[2]/div[1]/a
#//*[@id="shop-all-list"]/ul/li[14]/div[2]/div[1]/a.text
# num = 0
# for i in range(len(shop_list)):
	# shop_name = driver.find_element("//*[@id="shop-all-list"]/ul/li[%s]/div[2]/div[1]/a(%i).text")

time.sleep(4)