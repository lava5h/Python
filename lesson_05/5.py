from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/inputs")
      
input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    
# Ввод значения 1000
input_field.send_keys("1000")
print("Введено значение 1000")
    
# Очистка поля
input_field.clear()
print("Поле очищено")
    
# Ввод значения 999
input_field.send_keys("999")
print("Введено значение 999")
