from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(input1.text)
    y = calc(int(x))

    input2 = browser.find_element(By.CSS_SELECTOR, "#answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", input2)
    #Как вариант еще можно скрывать ненужный элемент
    # footer = browser.find_element(By.TAG_NAME, "footer")
    # browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)
    
    # Еще в глобальном смысле мотнуть в самый верх или самый низ страницы можно и питоном для тега body
    # from selenium.webdriver.common.keys import Keys
    # browser.find_element_by_tag_name('body').send_keys(Keys.END) #или Home если наверх
    
    input2.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()
    radiobuton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radiobuton.click()
    time.sleep(1)



    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()