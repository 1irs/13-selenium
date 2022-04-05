from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Открываем Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем страницу www.google.com
driver.get('https://www.google.com')

"""
<input class="gLFyf gsfi" jsaction="paste:puy29d;" maxlength="2048" name="q" 
type="text" aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" 
autocomplete="off" autocorrect="off" autofocus="" role="combobox" 
spellcheck="false" title="Search" value="" aria-label="Search" 
data-ved="0ahUKEwi84LSwrf32AhVMxoUKHdaBAecQ39UDCAQ">
"""

# Поиск по CSS-классу
search_field = driver.find_elements(By.CLASS_NAME, 'gLasdfasdfasdfFyf')

if len(search_field) == 0:
    print('Element with class name gLasdfasdfasdfFyf not found.')

# Поиск по атрибуту NAME
search_field_by_name = driver.find_elements(By.NAME, 'q')

# Поиск по тегу INPUT
search_field_by_tag = driver.find_element(By.TAG_NAME, 'input')

print('name==q count: ', len(search_field_by_name))


pass

