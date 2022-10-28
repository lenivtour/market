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
add_element = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click() # добавляем продукт в корзину

#time.sleep(5)
# смотрим, что в корзине появился товар
wait = WebDriverWait(driver, timeout=10)  # переменная для явного ожидания
add = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a>.amount'), '180'))

#-----------проверка корзины
check_price_basket = driver.find_element(By.CSS_SELECTOR, 'a>.amount').text
print(check_price_basket)
assert check_price_basket == '₹180.00'
check_items_basket = driver.find_element(By.CSS_SELECTOR, 'a>.cartcontents').text
print(check_items_basket)
assert check_items_basket == '1 Item'


# переходим в корзину и проверяем цены.
price = '180' # задал переменную для проверки цены
basket = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents').click()
subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'td[data-title = "Subtotal"]'), price))
print(subtotal)
total = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total td[data-title = "Total"]'), '183.60'))
print(subtotal)

driver.quit()