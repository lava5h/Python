# Руководство по работе с проектом
## Запуск тестов
## Предварительные требования
* Python (3.8+)
* Pytest
* Selenium
* Webdriver-manager
* Allure
## Установка библиотек
    pip install pytest 
    pip install selenium 
    pip install webdriver-manager
    pip install allure-pytest
## Основные команды
    # Переход к папке с тестами
      cd "путь к папке с тестами" 

    # Запуск конкретного теста
      pytest "название теста"

    # Запуск всех тестов в папке
      pytest
## Параметры запуска
    # Запуск теста и генерация отчета
      pytest --alluredir=./allure-result
## Просмотр отчетов
    # Просмотр отчёта
      allure serve reports/allure-results
