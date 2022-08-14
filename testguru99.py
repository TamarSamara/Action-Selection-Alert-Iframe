import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")


def startTest():
    url = "https://demo.guru99.com/test/newtours/register.php"
    driver.get(url)
    # time.sleep(3)


def login(**kwargs):

    driver.find_element(By.NAME, kwargs["param"]).send_keys(kwargs["name"])
    # time.sleep(3)



def test_automation():
    startTest()
    try:
        login(name="tamar", param="firstName")
        time.sleep(1)
        login(name="samara", param="lastName")
        time.sleep(1)
        login(name="0546837579", param="phone")
        time.sleep(1)
        login(name="tamar.samara@gmail.com", param="userName")
        time.sleep(1)
        login(name="Rama", param="address1")
        time.sleep(1)
        login(name="Rama", param="city")
        time.sleep(1)
        login(name="-", param="state")
        time.sleep(1)
        login(name="30055", param="postalCode")
        time.sleep(1)

        sel = driver.find_element(By.NAME, "country")
        select = Select(sel)
        # select.select_by_visible_text('ISRAEL')
        select.select_by_value('ISRAEL')
        time.sleep(1)
        login(name="tamar.samara@gmail.com", param="email")
        time.sleep(1)
        login(name="12345", param="password")
        time.sleep(1)
        login(name="12345", param="confirmPassword")
        time.sleep(1)

        driver.find_element(By.NAME, "submit").click()
        msg = driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font').text
        logging.warning('Error!')
        assert msg == "Dear tamar samara,"

    except Exception as e:
        print("error in code: {}".format(e))
    finally:
        time.sleep(3)

        driver.quit()

