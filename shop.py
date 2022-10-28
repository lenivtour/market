import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common.by import By  # импортируем By
from selenium.webdriver.support.select import Select    # импортируем класс селектор
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()  # полностью развернуть окно браузера
driver.implicitly_wait(10)# говорим WebDriver искать каждый элемент в течение 30 секунд
driver.get("https://practice.automationtesting.in") # открываем сайт

myaccount = driver.find_element(By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/my-account/"]').click()
username = driver.find_element(By.ID, 'username').send_keys('info@info.ru')
password = driver.find_element(By.ID, 'password').send_keys('asdfQWER1234!@#$')
login = driver.find_element(By.CSS_SELECTOR, 'input[name = "login"]').click()

log_out = driver.find_element(By.LINK_TEXT, 'Sign out').text

if log_out == 'Sign out':
    print('Sign out - actve')
else:
    print('Sign out NO')


shop = driver.find_element(By.ID, 'menu-item-40').click()        # заходим во вкладку shop
#time.sleep(2)
html_menu = driver.find_element(By.CSS_SELECTOR, 'li.cat-item.cat-item-19>a').click()  # клик на HTML слева

#time.sleep(2)
product_count = driver.find_elements(By.CSS_SELECTOR, 'li.product_cat-html')
print(len(product_count))   # ищем количество товаров в списке
if len(product_count) == 3:
    print('Найдено:', len(product_count), 'товаров')
else:
    print('найдено товаров не 3')



driver.quit()