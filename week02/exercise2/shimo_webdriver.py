from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://shimo.im")
    login_href = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button') 
    login_href.click()
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('120186766@qq.com')
    browser.find_element_by_xpath('//input[@name="password"]').send_keys('TEST000')
    login_button = browser.find_element_by_xpath('//button')
    login_button.click()
    time.sleep(10)
    print("login_success")
except Exception as e:
    print(e)
finally:
    browser.close()