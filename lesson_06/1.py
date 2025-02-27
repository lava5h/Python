from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/ajax")

# Кликаем на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

# Ожидание появления зелёной плашки
message = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
)

text = message.text

# Выводим текст
print(text)
