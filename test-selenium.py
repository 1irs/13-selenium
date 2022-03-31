# Подключаем библиотеку Селениум.
# Потому что в самом языке Python ничего про веб-тестирование нет.
# Селениум нужно скачать, установить, и подключить через import
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Класс Service служит для запуска и остановки ChromeDriver
service = Service(executable_path="/Users/obrizan/Projects/1IRS/selenium/chromedriver")

# Класс Chrome уже служит для того, чтобы управлять всеми возможностями браузера.
driver = webdriver.Chrome(service=service)

# Открыть браузер на нужной странице
driver.get('https://www.google.com')

