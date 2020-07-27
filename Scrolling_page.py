from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    
    x_element = browser.find_element_by_xpath ('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    print("Number: ", y)
    browser.execute_script("window.scrollBy(0, 200);") #скролл страницы
    time.sleep(1)
    element_1 = browser.find_element_by_xpath ('//*[@id="answer"]')
    element_1.send_keys (y)
    element_2 = browser.find_element_by_xpath ('//*[@id="robotCheckbox"]')
    element_2.click ()
    element_3 = browser.find_element_by_xpath ('//*[@id="robotsRule"]')
    element_3.click ()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print('Всё получилось. Тест пройден')
finally:

    time.sleep(5)
    browser.quit()

    
