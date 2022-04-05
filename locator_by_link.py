from get_driver import driver
from selenium.webdriver.common.by import By


# Открываем страницу www.google.com
driver.get('https://www.1irs.net/ru/education/selenium-python')

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'публічної')

pass
