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
driver.execute_script("window.scrollBy(0, 500);") # пролистываем страницу
selenium_ruby = driver.find_element(By.CSS_SELECTOR, 'a [title = "Selenium Ruby"]').click()
revies = driver.find_element(By.CLASS_NAME, 'reviews_tab').click()
star5 = driver.find_element(By.CLASS_NAME, 'star-5').click()
comment = driver.find_element(By.ID, 'comment').send_keys("Nice book!")
author = driver.find_element(By.ID, 'author').send_keys("Anton")
email = driver.find_element(By.ID, 'email').send_keys("info@info.ru")
driver.execute_script("window.scrollBy(0, 300);")
#time.sleep(2)
submit = driver.find_element(By.CLASS_NAME, 'submit').click()

driver.quit()