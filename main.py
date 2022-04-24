from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
# download chromedriver.exe to use it a service
driver = webdriver.Chrome(service=Service("C:/../chromedriver.exe"))
driver.get(URL)

time_to_buy = time.time() + 5
stop_time = time.time() + 5 * 60

while True:
    cookie = driver.find_element(by=By.ID, value="cookie")
    cookie.click()

    if time.time() >= time_to_buy:
        store_items = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        not_available = driver.find_elements(by=By.CSS_SELECTOR, value=".grayed b")
        # use list comprehension to retrieve the price from store selector

        available = [item for item in store_items if item not in not_available]
        # Purchase the most expensive item
        for item in available[::-1]:
            item.click()
            break

        time_to_buy = time.time() + 5

    if time.time() >= stop_time:
        cps = driver.find_element(by=By.ID, value="cps").text
        print(cps)
        break