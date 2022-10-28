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
driver.execute_script("window.scrollBy(0, 300);")
add_element = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]').click() # добавляем продукт в корзину
time.sleep(2)
basket = driver.find_element(By.CLASS_NAME, 'wpmenucart-contents').click() # переходим в корзину
checkout_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button'))).click() # оформляем заказ

#заполняем формы
driver.execute_script("window.scrollBy(0, 100);")
first_name = wait.until(EC.visibility_of_element_located((By.ID, 'billing_first_name'))).send_keys('Anton')
last_name = driver.find_element(By.ID, 'billing_last_name').send_keys('Gusev')
last_email = driver.find_element(By.ID, 'billing_email').send_keys('info@info.ru')
last_phone = driver.find_element(By.ID, 'billing_phone').send_keys('9998887766')
driver.execute_script("window.scrollBy(0, 100);")
country = driver.find_element(By.ID, 'select2-chosen-1').click()
country_select = driver.find_element(By.ID, 's2id_autogen1_search').send_keys('Russia')
country_confirm = driver.find_element(By.CLASS_NAME, 'select2-result-label').click()
adress = driver.find_element(By.CSS_SELECTOR, 'input#billing_address_1').send_keys('Tverskaya 1')
city = driver.find_element(By.CSS_SELECTOR, 'input#billing_city').send_keys('Moscow')
state = driver.find_element(By.CSS_SELECTOR, 'input#billing_state').send_keys('Moscow obl')
zip = driver.find_element(By.CSS_SELECTOR, 'input#billing_postcode').send_keys('134567')
driver.execute_script("window.scrollBy(0, 500);")
# вариант оплаты
payments = driver.find_element(By.CSS_SELECTOR, 'label[for="payment_method_cheque"]').click()
order = driver.find_element(By.ID, 'place_order').click()   # подтвердить
# Подтверждение успешной оплаты
succes_order = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
checkpay = driver.find_elements(By.CSS_SELECTOR, 'tfoot>tr>td')
for i in checkpay:
    a = (i.text)
    if a == 'Check Payments':
        print(a, 'Tect is OK!')
        break
    else:
        print('NO')
driver.quit()
