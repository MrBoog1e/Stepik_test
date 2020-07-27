from selenium import webdriver
from selenium.webdriver.support.ui import Select # для работы select = Select
import time
import math


print("Введите 1 или 2:", end=" ")
cnt = input()

def calc(x, y):
  return str(str((int(x)+int(y))))

try:
         link = "http://suninjuly.github.io/selects" + cnt + ".html"
         browser = webdriver.Chrome()
         browser.get(link)
    
         x_element = browser.find_element_by_xpath ('//*[@id="num1"]')
         x = x_element.text
         print("Число 1:", x)
         y_element = browser.find_element_by_xpath ('//*[@id="num2"]')
         y = y_element.text
         print("Число 2:", y)
         
         pops = calc(x, y)
         print("Сумма:", pops)
         
         select = Select(browser.find_element_by_tag_name("select"))
         select.select_by_value(pops) # ищем элемент с текстом 

         button = browser.find_element_by_css_selector("button.btn")
         button.click()
         
    
         print('Всё получилось. Тест пройден')
         
finally:

    time.sleep(5)
    browser.quit()
    
