import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from allure import step, title, description, feature, severity, severity_level

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from pages.page_shop import PageShop

shop_page = PageShop(driver)

# Авторизация
with step('Авторизация'):
    shop_page.autorization()

# Добавление товаров в корзину
with step('Добавление товаров в корзину'):
    shop_page.selection_of_goods()

# Переход в корзину и на вкладку с личной информацией
with step('Переход в корзину'):
    shop_page.cart_and_checkout_buttons()

# Ввод личной информации
with step('Ввод личной информации'):
    shop_page.personal_inf()

# Вывод итоговой стоимости
with step('Получение итоговой стоимости'):
    total = driver.find_element(By.CSS_SELECTOR, "div[data-test='total-label']").text
    print(total)

# Проверка
@feature('Оформление заказа')
@title('Тест проверки итоговой стоимости заказа')
@description('Этот тест проверяет корректность отображения итоговой стоимости заказа после добавления товаров и заполнения данных')
@severity(severity_level.CRITICAL)
def test_total():
    with step('Проверка корректности суммы'):
        assert total == 'Total: $58.29'
