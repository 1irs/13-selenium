from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем страницу www.google.com
driver.get('https://www.google.com')

driver.get('https://www.example.com')

driver.back()

driver.forward()

pass
