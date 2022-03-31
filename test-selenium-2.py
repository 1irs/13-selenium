from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем FireFox
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get('https://www.google.com')
