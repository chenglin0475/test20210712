from selenium import webdriver
import time

from selenium.webdriver.common.by import By

chromeDriver = webdriver.Chrome()
chromeDriver.get("http://localhost:8083/HKR")
chromeDriver.maximize_window()
chromeDriver.find_element_by_id("loginname").send_keys("15144804391")
chromeDriver.find_element_by_id("password").send_keys("123456")
chromeDriver.find_element_by_id("submit").click()
chromeDriver.find_element_by_xpath("//*[@name='time' and @class='show_tea']").send_keys("9（上晚自习）")
chromeDriver.find_element_by_xpath("//*[@name='teaName' and @class='show_tea']").send_keys("曹士明")
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[3]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[6]/td[2]/div/label[3]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[7]/td[3]/div/label[3]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[8]/td[2]/div/label[3]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[9]/td[2]/div/label[1]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[10]/td[3]/div/label[3]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[11]/td[2]/div/label[4]/div').click()
chromeDriver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[12]/td[2]/div/label[2]/div').click()
chromeDriver.find_element_by_id("textarea").send_keys("这还真没有啊")
time.sleep(5)
chromeDriver.find_element_by_id("subtn").click()
chromeDriver.quit()



