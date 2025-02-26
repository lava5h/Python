from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.CSS_SELECTOR, "input[id='username']")

# Ввод значения username
username.send_keys("tomsmith")
print("Введено значение tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "input[id='password']")

# Ввод значения password
password.send_keys("SuperSecretPassword!")
print("Введено значение SuperSecretPassword!")

# Нажатие на кнопку
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login.click()
