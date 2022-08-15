import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")


def startTest():
    url = "http://automationpractice.com/index.php"
    driver.get(url)

    # time.sleep(3)


def send_key(**kwargs):
    if "id" in kwargs.keys():
        driver.find_element(By.ID, kwargs["param"]).send_keys(kwargs["id"])
    elif "xpath" in kwargs.keys():
        driver.find_element(By.XPATH, kwargs["param"]).send_keys(kwargs["XPATH"])
    elif "name" in kwargs.keys():
        driver.find_element(By.NAME, kwargs["param"]).send_keys(kwargs["name"])
    elif "class_name" in kwargs.keys():
        driver.find_element(By.CLASS_NAME, kwargs["param"]).send_keys(kwargs["class_name"])

        # time.sleep(3)


def click_element(**kwargs):
    if "id" in kwargs.keys():
        driver.find_element(By.ID, kwargs["param"]).click()
    elif "xpath" in kwargs.keys():
        driver.find_element(By.XPATH, kwargs["param"]).click()
    elif "name" in kwargs.keys():
        driver.find_element(By.NAME, kwargs["param"]).click()
    elif "class_name" in kwargs.keys():
        driver.find_element(By.CLASS_NAME, kwargs["param"]).click()


def test_buy_dress():
    startTest()
    # click button sign in
    click_element(class_name="", param="login")
    # search summer
    send_key(id="summer", param="search_query_top")
    click_element(name="", param="submit_search")
    # click icon eye
    click_element(xpath="", param='//*[@id="center_column"]/ul/li[3]/div/div[1]/div/div[1]/a/i')
    time.sleep(4)

    # change iframe
    iframe = driver.find_element(By.CLASS_NAME, "fancybox-iframe")
    driver.switch_to.frame(iframe)

    # Click + to add more dresses
    click_element(xpath="", param='//*[@id="quantity_wanted_p"]/a[2]/span/i')
    time.sleep(3)
    # select M from dropdown
    sel = driver.find_element(By.ID, "group_1")
    select = Select(sel)
    select.select_by_value('2')
    click_element(id="", param="color_15")
    msg = driver.find_element(By.TAG_NAME, "h1").text
    logging.warning("Error!")
    assert msg == "Printed Chiffon Dress"

    # click add to cart
    click_element(xpath="", param='//*[@id="add_to_cart"]/button')

    time.sleep(3)
    driver.quit()
