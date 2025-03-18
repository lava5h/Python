from selenium.webdriver.common.by import By

class FormFiller:

    def __init__(self, driver):

        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Функция для заполнения полей
    def fill_form(self, data):

        for field, value in data.items():

            element = self.driver.find_element(By.CSS_SELECTOR, f"input[name='{field}']")
            element.send_keys(value)

    # Функция для нажатия кнопки
    def click_button(self):

        button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary")
        button.click()
