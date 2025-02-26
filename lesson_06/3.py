from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание загрузки всех картинок
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//p[text()='Done!']"))
)
    
# Получение 3-й картинки
images = driver.find_element(By.CSS_SELECTOR, "img[id='award']")
src = images.get_attribute("src")
    
# Вывод значения в консоль
print("Значение src 3-й картинки:", src)
