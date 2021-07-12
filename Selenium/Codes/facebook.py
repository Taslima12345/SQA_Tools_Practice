from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Edge("E:\Selenium\Driver\edgedriver_win64\msedgedriver.exe")

browser.get("http://www.facebook.com")

username = browser.find_element_by_id("email").send_keys("")
password = browser.find_element_by_id("pass").send_keys("")
submit   = browser.find_element_by_name("login").click()

wait = WebDriverWait( browser, 5 )
page_title = browser.title
assert page_title == "Face"



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# user_name = ""
# password = ""
# driver = webdriver.Edge("E:\Selenium\Driver\edgedriver_win64\msedgedriver.exe")
# driver.get("https://www.facebook.com")
# element = driver.find_element_by_id("email")
# element.send_keys(user_name)
# element = driver.find_element_by_id("pass")
# element.send_keys(password)
# element.send_keys(Keys.RETURN)
# element.close()

