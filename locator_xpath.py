from get_driver import driver
from selenium.webdriver.common.by import By


# Открываем страницу www.google.com
driver.get('https://www.1irs.net/ru/education/selenium-python')

full_xpath = '/html/body/div[2]/div[1]/div/div[2]/div/a'
short_xpath = '/html/body/div[2]/div[1]/div/div[2]/div/a'

link = driver.find_element(By.XPATH, full_xpath)

# XPATH
'/html/body/div[2]/div[4]/div[3]/h2'
'/html/body/div[2]/div[4]/div[3]/h2'
'/html/body/div[2]/div[4]/div[3]/h2'

# CSS SELECTOR
'body > div.container > div.row.gy-4.py-5.row-cols-1.row-cols-lg-3 > div:nth-child(3) > h2'

pass
