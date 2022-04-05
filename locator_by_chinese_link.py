from get_driver import driver
from selenium.webdriver.common.by import By


# Открываем страницу www.google.com
driver.get('http://localhost:9000')

link = driver.find_element(By.PARTIAL_LINK_TEXT, '上')

pass
