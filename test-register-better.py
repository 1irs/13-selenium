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


random_email = 'test' + str(random.randint(1, 1000000)) + '@example.com'
print('Имейл для регистрации: ', random_email)

# Выпишем, что мы хотим ввести в таблицу, и идентифакторы полей
# По сути — это массив кортежей (list of tuples),
# где в каждом кортеже по две записи.
test_data = [
    ('input-firstname',     'Vasya',        'First name'),
    ('input-lastname',      'Poupkind',     'Last name'),
    ('input-email',         random_email,   'Email'),
    ('input-telephone',     '123123'),
    ('input-password',      'asdfasdf'),
    ('input-confirm',       'asdfasdf'),
]

test_data_2 = {
    'input-firstname': 'Vasya',
    'input-lastname': 'Poupkind',
    'input-email': random_email,
    'input-telephone': '123123',
    'input-password': 'asdfasdf',
    'input-confirm': 'asdfasdf',
}


# 1. Идентифицируем все нужные элементы управления на странице.
agree_checkbox = driver.find_element(By.NAME, 'agree')
continue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')

# 2. Заполняем тестовыми данными.
# for form_element in test_data:
#     print('В поле', form_element[0], 'вводим', form_element[1])
#     elem = driver.find_element(By.ID, form_element[0])
#     elem.send_keys(form_element[1])
for key in test_data_2:
    print('В поле', key, 'вводим', test_data_2[key])
    elem = driver.find_element(By.ID, key)
    elem.send_keys(test_data_2[key])

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
