import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка браузера Selenium
driver = webdriver.Chrome()
url = "https://divan.ru/category/svet"
driver.get(url)

time.sleep(5)  # Ждем загрузки страницы

# Поиск элементов с товарами
svets = driver.find_elements(By.CLASS_NAME, "_Ud0k")

# Создаем или открываем CSV-файл для записи данных
with open("output.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["Название", "Цена", "Link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Парсинг информации о каждом товаре
    for svet in svets:
        name = svet.find_element(By.CLASS_NAME, "lsooF").find_element(By.TAG_NAME, "span").text
        price = svet.find_element(By.CLASS_NAME, "pY3d2").find_element(By.TAG_NAME, "span").text
        url = svet.find_element(By.TAG_NAME, "a").get_attribute("href")

        # Запись данных в CSV

        writer.writerow({
            "Название": name,
            "Цена": price,
            "Link": url
        })

# Закрытие браузера после выполнения задачи
driver.quit()
