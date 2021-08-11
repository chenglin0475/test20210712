from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.suning.com")
driver.maximize_window()
driver.find_elements_by_link_text("手机")[1].click()
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_link_text("华为").click()
data1 = driver.window_handles
driver.switch_to.window(data1[2])
time.sleep(3)
js1 = 'var action=document.documentElement.scrollTop=500'
# 设置滚动条距离顶部的位置，设置为 10000， 超过10000就是最底部
driver.execute_script(js1)  # 执行脚本
driver.find_element_by_link_text("华为 Mate 40 Pro 4G").click()
time.sleep(3)
data2 = driver.window_handles
driver.switch_to.window(data2[3])
js2 = 'var action=document.documentElement.scrollTop=1000'
driver.execute_script(js2)  # 执行脚本
driver.find_element_by_link_text("加入购物车").click()
time.sleep(3)
driver.quit()



