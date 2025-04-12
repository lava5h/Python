import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure import step, title, description, feature, severity, severity_level

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from pages.page_calc import PageCalc

page_calc = PageCalc(driver)

# Установка таймера
with step("Установка таймера"):
    page_calc.timer()

# Нажатие на кнопки калькулятора
with step("Нажатие на кнопки калькулятора"):
    page_calc.calc_buttons()

result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

@title("Проверка результата калькулятора")
@description("Тест проверяет правильность отображения результата в калькуляторе")
@feature("Калькулятор")
@severity(severity_level.CRITICAL)

# Проверка поля
def test_answer():
    with step("Получение результата из поля"):
        answer = driver.find_element(By.CSS_SELECTOR, ".screen").text
    
    with step("Проверка полученного результата"):
        assert answer == '15'
