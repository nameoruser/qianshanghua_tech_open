rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击搜索按钮
	adb shell input tap 1000 150
	ping -n 1 127.0.0.1>nul
	rem 搜索 pinkbear
	adb shell input text pinkbear
	ping -n 2 127.0.0.1>nul
	rem input click search after input text
	adb shell input tap 1006 167
	ping -n 2 127.0.0.1>nul
	rem 点击最热
	adb shell input tap 237 369
	ping -n 2 127.0.0.1>nul
	rem 点击图文
	adb shell input tap 975 355
	ping -n 2 127.0.0.1>nul
for /l %%i in (0,1,1000) do (
	echo %%i	
	rem 移动页面往上一小格
	adb shell input swipe 647 1458 647 883 2000
	ping -n 1 127.0.0.1>nul
	rem 点击第一张
	adb shell input tap 270 417
	ping -n 2 127.0.0.1>nul
	rem 点击分享按钮
	adb shell input tap 1010 170
	ping -n 2 127.0.0.1>nul
	rem 点击复制链接
	adb shell input tap 338 1894
	ping -n 2 127.0.0.1>nul
	rem 点击返回手机首页
	adb shell input tap 535 2300
	ping -n 2 127.0.0.1>nul
	rem 打开浏览器
	adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击复制栏
	adb shell input tap 300 462
	ping -n 2 127.0.0.1>nul
	rem 复制信息 
	rem adb shell input swipe 300 462 300 462 1000
	rem ping -n 2 127.0.0.1>nul
	rem 点击粘贴按钮
	adb shell input tap 468 1499
	ping -n 3 127.0.0.1>nul
	rem 点击submit
	adb shell input tap 333 681
	ping -n 3 127.0.0.1>nul
	rem 点击返回手机首页
	adb shell input tap 535 2300
	ping -n 2 127.0.0.1>nul
	rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 4 127.0.0.1>nul
	rem 点击返回
	adb shell input tap 772 2299
	ping -n 2 127.0.0.1>nul
	rem 点击第二张图片
	adb shell input tap 820 417
	ping -n 2 127.0.0.1>nul
	rem 点击分享按钮
	adb shell input tap 1010 170
	ping -n 2 127.0.0.1>nul
	rem 点击复制链接
	adb shell input tap 338 1894
	ping -n 2 127.0.0.1>nul
	rem 点击返回手机首页
	adb shell input tap 535 2300
	ping -n 2 127.0.0.1>nul
	rem 打开浏览器
	adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击复制栏
	adb shell input tap 300 462
	ping -n 2 127.0.0.1>nul
	rem 复制信息 
	rem adb shell input swipe 300 462 300 462 1000
	rem ping -n 2 127.0.0.1>nul
	rem 点击粘贴按钮
	adb shell input tap 468 1499
	ping -n 3 127.0.0.1>nul
	rem 点击submit
	adb shell input tap 333 681
	ping -n 2 127.0.0.1>nul
	rem 点击返回手机首页
	adb shell input tap 535 2300
	ping -n 2 127.0.0.1>nul
	rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 4 127.0.0.1>nul
	rem 点击返回
	adb shell input tap 772 2299
	ping -n 2 127.0.0.1>nul
)