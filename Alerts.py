#Alerts и как с ними жить
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn").click ()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_xpath ('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    element_1 = browser.find_element_by_xpath ('//*[@id="answer"]')
    element_1.click()
    element_1.send_keys (y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print('Всё получилось. Тест пройден')
finally:

    time.sleep(5)
    browser.quit()   
