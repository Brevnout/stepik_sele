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
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # Жмем кнопку
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()


    #Чтобы узнать имя новой вкладки - метод window_handles, возвращает массив имён всех вкладок:
    new_window = browser.window_handles[1]
    #Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
    first_window = browser.window_handles[0]
    #Текущую вкладку можно узнать так:
    current_window = browser.current_window_handle
    #Для переключения на новую вкладку switch_to.window:
    browser.switch_to.window(new_window)


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