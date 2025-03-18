import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Данные для заполнения полей
test_data = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "city": "Москва",
    "country": "Россия",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "job-position": "QA",
    "company": "SkyPro",
    "zip-code": ""
}

from pages.page_form import FormFiller

form_filler = FormFiller(driver)

# Заполнение полей
form_filler.fill_form(test_data)

# Нажатие кнопки
form_filler.click_button()

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
