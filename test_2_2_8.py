from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import os 


try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)



    input1 = browser.find_element(By.NAME, "firstname")    
    input1.send_keys("Tony")
    input2 = browser.find_element(By.NAME, "lastname")    
    input2.send_keys("Berl")
    input3 = browser.find_element(By.NAME, "email")    
    input3.send_keys("pochta@mail.ru")


    current_dir = os.path.abspath(os.path.dirname("test_2_2_8.py"))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    downloader = browser.find_element(By.CSS_SELECTOR, "#file")
    downloader.send_keys(file_path)


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