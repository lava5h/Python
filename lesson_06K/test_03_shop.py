import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("https://www.saucedemo.com/")

# Авторизация
username = driver.find_element(By.CSS_SELECTOR, "input[id='user-name']")
username.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, "input[id='password']")
password.send_keys("secret_sauce")

button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
button.click()

# Добавление товаров в корзину
add_backpack = driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']")
add_backpack.click()

add_t_short = driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']")
add_t_short.click()

add_onesie = driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']")
add_onesie.click()

# Переход в корзину
button_cart = driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
button_cart.click()

# Переход на вкладку с лисной информацией
button_checkout = driver.find_element(By.CSS_SELECTOR, "button[id='checkout']")
button_checkout.click()

# Ввод личной информации
firstname = driver.find_element(By.CSS_SELECTOR, "input[id='first-name']")
firstname.send_keys("Nikita")

lastname = driver.find_element(By.CSS_SELECTOR, "input[id='last-name']")
lastname.send_keys("Kazakov")

postalcode = driver.find_element(By.CSS_SELECTOR, "input[id='postal-code']")
postalcode.send_keys("000001")

button_continue = driver.find_element(By.CSS_SELECTOR, "input[id='continue']")
button_continue.click()

# Вывод итоговой стоимости
total = driver.find_element(By.CSS_SELECTOR, "div[data-test='total-label']").text
print(total)

driver.close()

# Проверка
def test_total():
    assert total == 'Total: $58.29'
