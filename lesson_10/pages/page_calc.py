from selenium.webdriver.common.by import By

class PageCalc:

    """
    Класс для работы с веб-калькулятором.
    
    Этот класс предоставляет методы для работы с элементами калькулятора.
    """

    def __init__(self, driver):

        """
        Инициализация страницы калькулятора.

        driver: объект веб-драйвера
        """

        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # Функция для установки таймера
    def timer(self):

        """
        Установка времени задержки для операций калькулятора.

        Метод находит поле ввода задержки, очищает его и устанавливает новое значение.
        """

        timer = self.driver.find_element(By.CSS_SELECTOR, "input[id='delay']")
        timer.clear()
        timer.send_keys("45")
    
    # Функция для нажатия кнопок калькулятора 
    def calc_buttons(self):

        """
        Нажатие кнопок на калькуляторе.

        Метод выполняет операцию: 7 + 8 =
        """

        button_7 = self.driver.find_element(By.XPATH, "//span[text()='7']")
        button_7.click()

        button_plus = self.driver.find_element(By.XPATH, "//span[text()='+']")
        button_plus.click()

        button_8 = self.driver.find_element(By.XPATH, "//span[text()='8']")
        button_8.click()

        button_equals = self.driver.find_element(By.XPATH, "//span[text()='=']")
        button_equals.click()
