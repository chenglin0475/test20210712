from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")
driver.maximize_window()
driver.find_element_by_link_text("亲，请登录").click()
driver.find_element_by_xpath("//*[@id='fm-login-id']").send_keys("15144804391")
driver.find_element_by_xpath("//*[@id='fm-login-password']").send_keys("cheng")
ac = ActionChains(driver) #事件链对象

driver.find_element_by_link_text("登录").click()
time.sleep(10)
driver.find_element_by_link_text("手机").click()
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_link_text("华为")
driver.find_element_by_xpath("//*[@id=['J_Itemlist_Pic_634868358842']")
driver.find_element_by_link_text("畅享20SE【4+128G】幻夜黑")
driver.find_element_by_link_text("官方标配")
driver.find_element_by_link_text("加入购物车")

time.sleep(3)
driver.quit()


