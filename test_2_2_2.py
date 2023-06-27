from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Ваш код, который заполняет обязательные поля



    input1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    input2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    x1 = int(input1.text)
    x2 = int(input2.text)
    y = str(x1+x2)

    answers = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    answers.select_by_value(y) # ищем элемент с текстом "Python"



    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()