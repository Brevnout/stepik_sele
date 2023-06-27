from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    browser.implicitly_wait(20)

    # Ожидпние пока элемент не удовлетворит условию и жмем кнопку
    price = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))    
    button_sub = browser.find_element(By.TAG_NAME, "button")
    button_sub.click()

    # заполняем форму
    input1 = browser.find_element(By.ID, "input_value")
    x = int(input1.text)
    y = calc(int(x))

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
    input1.get_attribute

  
    button_sub = browser.find_element(By.ID, "solve")
    button_sub.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы



finally:
    # получаем значение текста из alert
    #print(browser.switch_to.alert.text.split(': ')[-1])
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()