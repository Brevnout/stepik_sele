from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля ( вместо placeholder или атрибута required, выбрана привязка по label)
    input1 = browser.find_element(By.XPATH, "//label[contains(text(),'First name*')]/following-sibling::*")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//label[contains(text(),'Last name*')]/following-sibling::*")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//label[contains(text(),'Email*')]/following-sibling::*")
    input3.send_keys("ivan@mail.ru")

    # input4 = browser.find_element(By.XPATH, "//label[contains(text(),'Phone:')]/following-sibling::*")
    # input4.send_keys("555-55-55")
    # input5 = browser.find_element(By.XPATH, "//label[contains(text(),'Address:')]/following-sibling::*")
    # input5.send_keys("Russia, Omsk, Gagarin st., 15")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()