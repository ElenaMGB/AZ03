# 3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, 
# обработать данные, 
# найти среднюю цену и вывести ее, 
# а также сделать гистограмму цен на диваны​ 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# import time
import csv

# Настройка драйвера 
driver = webdriver.Firefox()

# URL страницы для парсинга
url = "https://www.divan.ru/ekaterinburg/category/divany-i-kresla"

# Открытие страницы
driver.get(url)

# Ожидание загрузки элементов с ценами
wait = WebDriverWait(driver, 10)
price_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-card__price")))

# Парсинг и вывод цен
for element in price_elements:
    price = element.text.strip()
    # print(f"Цена: {price}")

# Сохранение данных в CSV
with open('prices1.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Заголовки столбцов

# Записываем цены в CSV файл
    for price in price_elements:
        writer.writerow([price.text])

# Закрытие браузера
driver.quit()
