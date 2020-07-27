from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID , 'price'), "100")
        )
    button = browser.find_element_by_xpath ('//*[@id="book"]')
    button.click()
    browser.execute_script("window.scrollBy(0, 300);") #скролл страницы
    x_element = browser.find_element_by_xpath ('//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    pollwride = browser.find_element_by_xpath ('//*[@id="answer"]')
    pollwride.click()
    pollwride.send_keys (y)
    
    button = browser.find_element_by_xpath ('//*[@id="solve"]')
    button.click()

    # Копирование числа из алерта в терминал
    alert = browser.switch_to.alert
    alert_text = alert.text
    print (alert_text)
    
    print('Всё получилось. Тест пройден')

finally:

    time.sleep(5)
    browser.quit()

    
