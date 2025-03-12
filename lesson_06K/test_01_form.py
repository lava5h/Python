import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

# Заполняем поля
firstname = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
firstname.send_keys("Иван")
print("Введено значение Иван")

lastname = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
lastname.send_keys("Петров")
print("Введено значение Петров")

address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
address.send_keys("Ленина, 55-3")
print("Введено значение Ленина, 55-3")

city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
city.send_keys("Москва")
print("Введено значение Москва")

country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
country.send_keys("Россия")
print("Введено значение Россия")

email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
email.send_keys("test@skypro.com")
print("Введено значение test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
phone.send_keys("+7985899998787")
print("Введено значение +7985899998787")

job = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
job.send_keys("QA")
print("Введено значение QA")

company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
company.send_keys("SkyPro")
print("Введено значение SkyPro")

zip = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
company.send_keys(" ")
print("Введено значение  ")

# Нажатие на кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary")
button.click()

# Проверка полей
@pytest.mark.parametrize("field_id, expected_class", [
    ("first-name", "alert py-2 alert-success"),
    ("last-name", "alert py-2 alert-success"),
    ("zip-code", "alert py-2 alert-danger"),
    ("address", "alert py-2 alert-success"),
    ("city", "alert py-2 alert-success"),
    ("country", "alert py-2 alert-success"),
    ("e-mail", "alert py-2 alert-success"),
    ("job-position", "alert py-2 alert-success"),
    ("phone", "alert py-2 alert-success"),
    ("company", "alert py-2 alert-success"),
])
def test_fields(field_id, expected_class):
    field_element = driver.find_element(By.CSS_SELECTOR, f"div[id='{field_id}']")
    field_class = field_element.get_attribute("class")
    assert field_class == expected_class
