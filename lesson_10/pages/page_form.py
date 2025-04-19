from selenium.webdriver.common.by import By

class FormFiller:

    """
    Класс для работы с веб-формой.
    
    Этот класс предоставляет методы для заполнения полей формы и отправки данных.
    """

    def __init__(self, driver):

        """
        Инициализация страницы формы.

        driver: объект веб-драйвера
        """

        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    # Функция для заполнения полей
    def fill_form(self, data):

        """
        Заполнение полей формы данными.

        data: словарь с данными
        """

        for field, value in data.items():

            element = self.driver.find_element(By.CSS_SELECTOR, f"input[name='{field}']")
            element.send_keys(value)

    # Функция для нажатия кнопки
    def click_button(self):

        """
        Нажатие на кнопку отправки формы.
        """

        button = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary")
        button.click()
