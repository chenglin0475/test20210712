
# encoding=utf-8
from appium import webdriver
import  time
server = r'http://localhost:4723/wd/hub'      # Appium Server, 端口默认为4723
desired_capabilities = {
    'platformName': 'Android',    # 平台
    # 需替换成你的driverName，如果不知 道自己的设备名，用adb命令去查看一下
    'deviceName': '127.0.0.1:62001',
    'platformVersion': '7.1.2',      # 安卓版本
    'appPackage': 'com.ss.android.ugc.aweme',      #APP包名
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity' ,      # APP启动名
    'unicodeKeyboard': True,       # 这句和下面那句是避免中文问题的
    'resetKeyboard': True
}
driver = webdriver.Remote(server, desired_capabilities) # 连接手机和APP
time.sleep(3)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click() # 定位并点击
time.sleep(2)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click() # 定位并点击
time.sleep(2)
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click() # 定位并点击
def deep():
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    # 向左滑动
    driver.swipe(x * 0.5, y * 0.8, x * 0.5, y * 0.2, duration=2000)




while True:
    try:
        deep()
        time.sleep(3)
    except Exception as e:
        print(str(e))
        break
        pass
driver.quit()

