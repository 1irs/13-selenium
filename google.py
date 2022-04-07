from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем страницу www.google.com
driver.get('https://www.google.com')

# Поиск по атрибуту NAME
search_field_by_name = driver.find_element(By.NAME, 'q')

search_field_by_name.send_keys('selenium'+Keys.LEFT)

driver.close()
