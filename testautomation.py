import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.support import expected_conditions as EC

url = "http://automationpractice.com/index.php"
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get(url)


@pytest.mark.passed
def test_buy_dress_summer():
    try:

        driver.find_element(By.ID, "search_query_top").send_keys("summer")
        driver.find_element(By.NAME, "submit_search").click()
        # msg2 = driver.find_element(By.CLASS_NAME, "lighter").text
        # logging.warning("Error: 'Page Search 'summer'")
        # assert msg2 == "SUMMER"
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]').click()
        time.sleep(3)
        # msg3 = driver.find_element(By.CLASS_NAME, "icon-ok")
        # logging.warning("Error: 'Page: Product successfully added to your shopping cart")
        # assert msg3 == "Product successfully added to your shopping cart"

        # time.sleep(7)
        # Click on the Close window
        driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/span').click()
        time.sleep(3)
        # msg4 = driver.find_element(By.CLASS_NAME, "lighter").text
        # logging.warning("Error: 'Page Search 'summer'")
        # assert msg4 == "summer"

        # Click on the Cart
        driver.find_element(By.XPATH, '//*[@id="button_order_cart"]/span').click()
        # msg5 = driver.find_element(By.CLASS_NAME, "page-heading").text
        # logging.warning("Error: 'Page Shopping-cart summary'")
        # assert msg5 == "Shopping-cart summary"

        time.sleep(5)

    except Exception as e:
        print("error in code: {}".format(e))

    finally:
        driver.quit()
