from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge("E:\Selenium\Driver\edgedriver_win64\msedgedriver.exe")

# driver.get("http://dhakamovie.com/")
# driver.find_element_by_id("inputString").send_keys("Movies")

driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Selenium")
# driver.find_element_by_name("btnK").click()
# driver.find_element_by_class_name("gNO89b").click()
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]").click()