from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
    
# Ожидание появления модального окна
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.modal"))
)

# Найти кнопку Close и нажать на неё
close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer")
close_button.click()
