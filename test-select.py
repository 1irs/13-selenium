from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://localhost:9000')

select_element = driver.find_element(By.ID, 'cars')
select_object = Select(select_element)

select_object.select_by_index(1)

select_object.select_by_value('audi')
select_object.select_by_visible_text('Volvo')

driver.close()
