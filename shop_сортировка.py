import time
from selenium import webdriver # импортируем webdriver
from selenium.webdriver.common.by import By  # импортируем By
from selenium.webdriver.support.select import Select    # импортируем класс селектор
from selenium.webdriver.support.ui import WebDriverWait #
from selenium.webdriver.support import expected_conditions as EC #
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
    print('Вы не залогинились')


shop = driver.find_element(By.ID, 'menu-item-40').click()        # заходим во вкладку shop
sorter = driver.find_element(By.CSS_SELECTOR, 'option[selected]').text # находим фильтр и смотрим его текст
if sorter == 'Default sorting':
    print("значение кнопки:", sorter)  # печатаем значение
else:
    print('Селектор не по умолчанию')

sorter2 = driver.find_element(By.CSS_SELECTOR, 'select.orderby')    # поиск селектора
sorter2_status = Select(sorter2)
sorter2_status.select_by_visible_text('Sort by price: high to low')   # устанавливаем селектор статус
sorter_check = driver.find_element(By.CSS_SELECTOR, 'option[selected]').text # находим фильтр и смотрим его текст
#print("значение кнопки:", sorter_check)
if sorter_check == 'Sort by price: high to low':
    print("значение кнопки:", sorter_check)  # печатаем значение
else:
    print('Селектор не установлен')

driver.quit()