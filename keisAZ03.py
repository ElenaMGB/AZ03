from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Инициализация драйвера
driver = webdriver.Firefox()


# URL сайта для парсинга
# url = "https://ekb.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/"
url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'
driver.get(url)

# Ожидание загрузки страницы
time.sleep(5)  # Можно использовать WebDriverWait для более надежного ожидания

# Парсинг цен
# prices = driver.find_elements(By.XPATH, "//div[@data-name='GeneralInfoSectionRowComponent']//span[@data-mark='MainPrice']//span")  # XPath для цен
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")

# Сохранение данных в CSV
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовки столбцов

# Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()
