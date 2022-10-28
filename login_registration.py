import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common.by import By  # импортируем By
from selenium.webdriver.support.select import Select # импортируем класс селектор
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()  # полностью развернуть окно браузера
driver.implicitly_wait(10)# говорим WebDriver искать каждый элемент в течение 30 секунд
driver.get("https://practice.automationtesting.in") # открываем сайт

myaccount = driver.find_element(By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/my-account/"]').click()
email = driver.find_element(By.ID, 'reg_email').send_keys('info@info.ru')
password = driver.find_element(By.ID, 'reg_password').send_keys('asdfQWER1234!@#$')
register = driver.find_element(By.CSS_SELECTOR, 'input[name = "register"]').click()

driver.quit()