import os
num = 1
end_num = 10
while True:
    os.system("adb -s aeebf218 shell input swipe 421 689 421 1752")
    os.system("ping -n 1 127.0.0.1>nul")
    for i in range (num,end_num):
      os.system("adb -s aeebf218 shell input tap 303 1399")
      os.system("ping -n 2 127.0.0.1>nul")
      os.system("adb -s aeebf218 shell input swipe 902 971 213 608")
      os.system("ping -n 1 127.0.0.1>nul")
      os.system("adb -s aeebf218 shell input swipe 902 971 213 608")
      os.system("ping -n 1 127.0.0.1>nul")
      os.system("adb -s aeebf218 shell input tap 70 180")
      os.system("ping -n 1 127.0.0.1>nul")

    # os.system("adb -s aeebf218 shell input swipe 421 689 421 1752")
    # os.system("ping -n 1 127.0.0.1>nul")
    # for i in range (num,end_num):
    #     os.system("adb -s aeebf218 shell input tap 303 1399")
    #     os.system("ping -n 7 127.0.0.1>nul")
    #     os.system("adb -s aeebf218 shell input tap 70 180")
    #     os.system("ping -n 1 127.0.0.1>nul")
