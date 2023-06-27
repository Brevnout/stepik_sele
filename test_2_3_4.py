from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import os 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    # Жмем кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Переключаемся на алерт и жмем ОК
    alert = browser.switch_to.alert
    alert.accept()


    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = input1.text
    y = calc(int(x))
    
    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")    
    input2.send_keys(y)

    button_sub = browser.find_element(By.TAG_NAME, "button")
    button_sub.click()  

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # получаем значение текста из alert
    print(browser.switch_to.alert.text.split(': ')[-1])
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()