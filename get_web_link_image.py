#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os
import requests
import time
img_list = [ 
    "https://bkimg.cdn.bcebos.com/pic/a8773912b31bb0511d63a3b3367adab44bede0e2?x-bce-process=image/resize,m_lfit,w_440,limit_1/format,f_auto",
]
num = 0
for img in img_list:
    num = num + 1
    img_uri = img
    print(img_uri)
    img_url = img_uri
    img_response = requests.get(img_url)
    t = int(time.time())
    f = open(os.path.join(os.path.dirname(__file__),'./files/%s_%s.%s'%(num,t,"jpg")), "ab")
    f.write(img_response.content)  # 多媒体存储content
    f.close()