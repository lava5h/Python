import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

# Установка таймера
timer = driver.find_element(By.CSS_SELECTOR, "input[id='delay']")
timer.clear()
timer.send_keys("45")

# Нажатие на кнопки калькулятора
button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
button_7.click()

button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
button_plus.click()

button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
button_8.click()

button_equals = driver.find_element(By.XPATH, "//span[text()='=']")
button_equals.click()

result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

# Проверка поля
def test_answer():
    answer = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert answer == '15' 
