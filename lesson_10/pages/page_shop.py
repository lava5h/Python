from selenium.webdriver.common.by import By

class PageShop:

    """
    Класс для работы с веб-приложением интернет-магазина.
    
    Предоставляет методы для авторизации, работы с товарами и оформления заказа.
    """

    def __init__(self, driver):

        """
        Инициализация страницы магазина.

        driver: объект веб-драйвера
        """

        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    # Функция для авторизации
    def autorization(self):

        """
        Выполнение авторизации в системе.
        """

        username = self.driver.find_element(By.CSS_SELECTOR, "input[id='user-name']")
        username.send_keys("standard_user")

        password = self.driver.find_element(By.CSS_SELECTOR, "input[id='password']")
        password.send_keys("secret_sauce")

        button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
        button.click()  

    # Функция для добавления товаров в корзину
    def selection_of_goods(self):

        """
        Добавление товаров в корзину.
        """

        add_backpack = self.driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-backpack']")
        add_backpack.click()

        add_t_short = self.driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']")
        add_t_short.click()

        add_onesie = self.driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']")
        add_onesie.click()

    # Функция нажатия кнопок для перехода в корзину и на вкладку с личной информацией
    def cart_and_checkout_buttons(self):

        """
        Переход в корзину и на страницу оформления заказа.
        """

        button_cart = self.driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
        button_cart.click()

        button_checkout = self.driver.find_element(By.CSS_SELECTOR, "button[id='checkout']")
        button_checkout.click()

    # Функция для ввода личной информации
    def personal_inf(self):

        """
        Заполнение формы личной информации.
        """

        firstname = self.driver.find_element(By.CSS_SELECTOR, "input[id='first-name']")
        firstname.send_keys("Nikita")

        lastname = self.driver.find_element(By.CSS_SELECTOR, "input[id='last-name']")
        lastname.send_keys("Kazakov")

        postalcode = self.driver.find_element(By.CSS_SELECTOR, "input[id='postal-code']")
        postalcode.send_keys("000002")

        button_continue = self.driver.find_element(By.CSS_SELECTOR, "input[id='continue']")
        button_continue.click()
    