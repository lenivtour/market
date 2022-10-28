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


#________________открываем сайт , входим по по логину и паролю
myaccount = driver.find_element(By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/my-account/"]').click()
username = driver.find_element(By.ID, 'username').send_keys('info@info.ru')
password = driver.find_element(By.ID, 'password').send_keys('asdfQWER1234!@#$')
login = driver.find_element(By.CSS_SELECTOR, 'input[name = "login"]').click()
log_out = driver.find_element(By.LINK_TEXT, 'Sign out').text
if log_out == 'Sign out':
    print('Sign out - actve')
else:
    print('Вы не залогинились')
#_____________________________________________________________-
shop = driver.find_element(By.ID, 'menu-item-40').click()        # заходим во вкладку shop
android_click = driver.find_element(By.PARTIAL_LINK_TEXT, 'Android Quick Start Guide').click()

#__________проверка цен:
delprice = driver.find_element(By.CSS_SELECTOR, 'del .amount').text
print(delprice)
assert delprice == '₹600.00'
insprice = driver.find_element(By.CSS_SELECTOR, 'ins .amount').text
print(insprice)
assert insprice == '₹450.00'
#_______________________
image = driver.find_element(By.CSS_SELECTOR, 'div.images').click()
closebtn = WebDriverWait(driver, timeout=30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
closebtn.click()

driver.quit()