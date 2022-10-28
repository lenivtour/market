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

wait = WebDriverWait(driver, timeout=10)  # переменная для явного ожидания

myaccount = driver.find_element(By.CSS_SELECTOR, 'a[href="https://practice.automationtesting.in/my-account/"]').click()   #открываем сайт
shop = driver.find_element(By.ID, 'menu-item-40').click()    # заходим во вкладку shop

add_element = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click() # добавляем продукт в корзину
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")
add_element = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="180"]').click() # добавляем продукт в корзину

add = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'a>.cartcontents'), '2 Items')) # до появления текста 2 items
basket = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents').click() # переходим в корзину

time.sleep(2)
del_element = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click()
undo = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Undo?'))).click()

quantity = driver.find_element(By.CSS_SELECTOR, '.quantity input:nth-child(1)').clear() # очищаем поле
quantity = driver.find_element(By.CSS_SELECTOR, '.quantity input:nth-child(1)').send_keys(3) # увеличиваем количество на 3
update = driver.find_element(By.CSS_SELECTOR, 'input[value="Update Basket"]').click() # обновить корзину
check_quantity = driver.find_element(By.CSS_SELECTOR, '.quantity input:nth-child(1)').get_attribute('value') # проверяем колличество
print(check_quantity)
assert check_quantity == '3'
time.sleep(2)
app_coupon = driver.find_element(By.CSS_SELECTOR, '[name="apply_coupon"]').click() # применить купон
coupon_code = driver.find_element(By.CSS_SELECTOR, '.woocommerce li').text # проверяем текст
print(coupon_code)
assert coupon_code == 'Please enter a coupon code.'


driver.quit()
