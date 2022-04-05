from selenium.webdriver.remote.webelement import WebElement

from get_driver import driver
from selenium.webdriver.common.by import By


# Открываем страницу www.google.com
driver.get('https://www.google.com')

search_input = driver.find_element(By.CSS_SELECTOR, '[title=Search]')

driver.get('https://www.1irs.net/ru/education/selenium-python')

elem = driver.find_element(By.CSS_SELECTOR, 'ol:first-child')

pass
