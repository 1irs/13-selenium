from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем страницу www.google.com
driver.get('http://localhost:9000/')

text_area = driver.find_element(By.CLASS_NAME, 'w3review')

text_area.clear()

text_area.send_keys("""hello world
multiple line
of
text""")
# search_box = driver.find_element(By.NAME, 'q')
# search_box.send_keys('selenium')
# search_box.send_keys(Keys.LEFT)
# search_box.send_keys(Keys.LEFT)
# search_box.send_keys(Keys.LEFT)
# search_box.send_keys(Keys.BACKSPACE)
# search_box.send_keys(Keys.BACKSPACE)
# search_box.send_keys('w')

driver.close()

