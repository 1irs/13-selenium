from selenium.webdriver.remote.webelement import WebElement

from get_driver import driver
from selenium.webdriver.common.by import By


# Открываем страницу www.google.com
driver.get('https://www.1irs.net/ru/education/selenium-python')

# Здесь помогает Селениум
all_headers = driver.find_elements(By.TAG_NAME, 'h1')

# Чистый Питон
for header in all_headers:
    print(header.text)  # Здесь Селениум помогает достать текст тега.

pass
