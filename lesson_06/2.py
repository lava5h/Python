from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открываем страницу
driver.get("http://uitestingplayground.com/textinput")

mybutton = driver.find_element(By.CSS_SELECTOR, "input[id='newButtonName']")

# Ввод значения username
mybutton.send_keys("SkyPro")
print("Введено значение SkyPro")

# Кликаем на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
button.click()

# Проверяем изменилось ли название кнопки и кликаем на неё 
newbutton = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
skypro_button = newbutton.text
print(skypro_button)
newbutton.click()
