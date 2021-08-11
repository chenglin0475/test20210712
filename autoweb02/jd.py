from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.jd.com")
driver.maximize_window()
driver.find_element_by_link_text("你好，请登录").click()
driver.find_element_by_link_text("账户登录").click()
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("不止于此0475")
driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("chenglin123.")
driver.find_element_by_xpath("//*[@id='loginsubmit']").click()
# e = driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")
# ac = ActionChains(driver)
# ac.click_and_hold(e).move_by_offset(80,0).perform()
time.sleep(10)
driver.find_element_by_link_text("手机").click()
data1 = driver.window_handles
driver.switch_to.window(data1[1])
driver.find_element_by_link_text("华为").click()
data2 = driver.window_handles
driver.switch_to.window(data2[2])
driver.find_element_by_link_text("nova系列").click()
time.sleep(3)
js = 'var action=document.documentElement.scrollTop=500'
# 设置滚动条距离顶部的位置，设置为 10000， 超过10000就是最底部
driver.execute_script(js)  # 执行脚本


driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
time.sleep(5)
driver.quit()




