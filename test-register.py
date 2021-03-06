# http://tutorialsninja.com/demo/
import random
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

start = time.time()

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открыть страницу с регистрацией
driver.get('http://tutorialsninja.com/demo/index.php?route=account/register')

# 1. Идентифицируем все нужные элементы управления на странице.
firstname_input = driver.find_element(By.ID, 'input-firstname')
lastname_input = driver.find_element(By.ID, 'input-lastname')
email_input = driver.find_element(By.ID, 'input-email')
phone_input = driver.find_element(By.ID, 'input-telephone')
password_input = driver.find_element(By.ID, 'input-password')
password2_input = driver.find_element(By.ID, 'input-confirm')

agree_checkbox = driver.find_element(By.NAME, 'agree')

continue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')

# 2. Заполняем тестовыми данными.
firstname_input.send_keys('Vasya')
lastname_input.send_keys('Poupkind')

random_email = 'test' + str(random.randint(1, 1000000)) + '@example.com'
print('Имейл для регистрации: ', random_email)

email_input.send_keys(random_email)
phone_input.send_keys('149521')
password_input.send_keys('asdfasdf')
password2_input.send_keys('asdfasdf')

# 3. Кликаем чекбокс "Agree to privacy policy"
agree_checkbox.click()

# 4. Кликаем "Continue"
continue_button.click()

# Проверяем, прошла ли регистрация:
all_h1_tags = driver.find_elements(By.TAG_NAME, 'h1')

if all_h1_tags[1].text == 'Your Account Has Been Created!':
    print('✅ Тест успешно прошел.')
else:
    print('❌ Тест провален.')

driver.close()

finish = time.time()

print('Тест прошел за ' + str(int(finish-start)) + ' сек.')
