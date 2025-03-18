import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from pages.page_shop import PageShop

shop_page = PageShop(driver)

# Авторизация
shop_page.autorization()

# Добавление товаров в корзину
shop_page.selection_of_goods()

# Переход в корзину и на вкладку с личной информацией
shop_page.cart_and_checkout_buttons()

# Ввод личной информации
shop_page.personal_inf()

# Вывод итоговой стоимости
total = driver.find_element(By.CSS_SELECTOR, "div[data-test='total-label']").text
print(total)

# Проверка
def test_total():
    assert total == 'Total: $58.29'
