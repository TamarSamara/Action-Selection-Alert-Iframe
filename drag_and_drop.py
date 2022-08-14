import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = 'https://demo.guru99.com/test/drag_drop.html'
driver.get(url)


def sor_tar(source_element, target_element):
    action = ActionChains(driver)
    action.drag_and_drop(source_element, target_element)
    action.perform()
    time.sleep(2)


def test_drag_and_drop():
    try:
        # 5000
        source_element = driver.find_element(By.XPATH, '//*[@id="fourth"]/a')
        target_element = driver.find_element(By.ID, "amt7")
        sor_tar(source_element, target_element)

        # 5000:
        source_element = driver.find_element(By.XPATH, '//*[@id="fourth"]/a')
        target_element = driver.find_element(By.ID, "amt8")
        sor_tar(source_element, target_element)

        # bank
        source_element = driver.find_element(By.ID, "credit2")
        target_element = driver.find_element(By.ID, "bank")
        sor_tar(source_element, target_element)

        # Sales
        source_element = driver.find_element(By.ID, "credit1")
        target_element = driver.find_element(By.ID, "loan")
        sor_tar(source_element, target_element)

        # perfect
        perButt = driver.find_element(By.XPATH, '//*[@id="equal"]/a')
        boolPer = perButt.is_displayed()
        logging.warning(f' Error! ')
        assert boolPer == True
        perButt.click()
        time.sleep(3)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()
