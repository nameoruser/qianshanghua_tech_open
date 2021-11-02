 rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击搜索按钮
	adb shell input tap 992 181
	ping -n 1 127.0.0.1>nul
	rem 搜索 puco
	adb shell input text puco
	ping -n 2 127.0.0.1>nul
	rem 点击搜索按钮
	adb shell input tap 1002 164
	ping -n 4 127.0.0.1>nul
for /l %%i in (0,1,5) do (
	echo %%i
	rem 移动页面往上一小格
	adb shell input swipe 750 1864 750 1099 2000
	rem 点击第一个点
	adb shell input tap 276 350
	ping -n 4 127.0.0.1>nul	
if a = news(
	adb shell input tap 995 166
	ping -n 4 127.0.0.1>nul
	rem 点击复制链接
	adb shell input tap 356 1854
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 打开浏览器
	adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 刷新浏览器
	adb shell input tap 950 161
	ping -n 4 127.0.0.1>nul
	rem 点击粘贴框
	adb shell input tap 234 490
	ping -n 4 127.0.0.1>nul
	rem 粘贴信息
	adb shell input swipe 234 490 234 490 1000
	ping -n 2 127.0.0.1>nul
	rem 点击粘贴
	adb shell input tap 128 339
	ping -n 4 127.0.0.1>nul
	rem 点击submit
	adb shell input tap 355 736
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击返回
	adb shell input tap 80 166
	ping -n 4 127.0.0.1>nul
)else if (
	rem 点击分享图标
	adb shell input tap 995 166
	ping -n 4 127.0.0.1>nul
	rem 点击复制链接
	adb shell input tap 580 1844
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 打开浏览器
	adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 刷新浏览器
	adb shell input tap 950 161
	ping -n 4 127.0.0.1>nul
	rem 点击粘贴框
	adb shell input tap 718 490
	ping -n 4 127.0.0.1>nul
	rem 粘贴信息
	adb shell input swipe 718 490 718 490 1000
	ping -n 2 127.0.0.1>nul
	rem 点击粘贴
	adb shell input tap 560 335
	ping -n 4 127.0.0.1>nul
	rem 点击submit
	adb shell input tap 750 730
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击返回
	adb shell input tap 80 166
	ping -n 4 127.0.0.1>nul
)
	rem 点击第二个点
	adb shell input tap 826 350
	ping -n 4 127.0.0.1>nul
if a = video(
	rem 点击分享图标
	adb shell input tap 995 166
	ping -n 4 127.0.0.1>nul
	rem 点击复制链接
	adb shell input tap 580 1844
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 打开浏览器
	adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 刷新浏览器
	adb shell input tap 950 161
	ping -n 4 127.0.0.1>nul
	rem 点击粘贴框
	adb shell input tap 718 490
	ping -n 4 127.0.0.1>nul
	rem 粘贴信息
	adb shell input swipe 718 490 718 490 1000
	ping -n 2 127.0.0.1>nul
	rem 点击粘贴
	adb shell input tap 560 335
	ping -n 4 127.0.0.1>nul
	rem 点击submit
	adb shell input tap 750 730
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击返回
	adb shell input tap 80 166
	ping -n 4 127.0.0.1>nul
)else if(
	rem 点击分享图标
	adb shell input tap 995 166
	ping -n 4 127.0.0.1>nul
	rem 点击复制链接
	adb shell input tap 580 1844
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 打开浏览器
	adb shell monkey -p com.android.browser -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 刷新浏览器
	adb shell input tap 950 161
	ping -n 4 127.0.0.1>nul
	rem 点击粘贴框
	adb shell input tap 718 490
	ping -n 4 127.0.0.1>nul
	rem 粘贴信息
	adb shell input swipe 718 490 718 490 1000
	ping -n 2 127.0.0.1>nul
	rem 点击粘贴
	adb shell input tap 560 335
	ping -n 4 127.0.0.1>nul
	rem 点击submit
	adb shell input tap 750 730
	ping -n 4 127.0.0.1>nul
	rem 点击返回桌面
	adb shell input tap 527 2282
	ping -n 4 127.0.0.1>nul
	rem 自动打开小红书
	adb shell monkey -p com.xingin.xhs -c android.intent.category.LAUNCHER 1
	ping -n 5 127.0.0.1>nul
	rem 点击返回
	adb shell input tap 80 166
	ping -n 4 127.0.0.1>nul
)
)
