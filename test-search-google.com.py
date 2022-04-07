from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. Открываем страницу www.google.com
driver.get('https://www.google.com')

# 2. Ищем по ключевому слову Selenium
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('hello' + Keys.ENTER)

# 3. В результате поиска первый результат должен быть selenium.dev
search_result_urls_elements = driver.find_elements(By.TAG_NAME, 'cite')

# Проверить страницу с результатами поиска.
if search_result_urls_elements[0].text == 'https://www.selenium.dev':
    print('✅ Тест успешно прошел.')
else:
    print('❌ Тест провален.')

# Закрыть браузер.
driver.close()
