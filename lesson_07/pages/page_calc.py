from selenium.webdriver.common.by import By

class PageCalc:

    def __init__(self, driver):

        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Функция для установки таймера
    def timer(self):

        timer = self.driver.find_element(By.CSS_SELECTOR, "input[id='delay']")
        timer.clear()
        timer.send_keys("45")
    
    # Функция для нажатия кнопок калькулятора 
    def calc_buttons(self):
        button_7 = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        button_plus = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        button_8 = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

        button_equals = self.driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()
