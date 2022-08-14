import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.alert import Alert

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = 'http://the-internet.herokuapp.com/javascript_alerts'
driver.get(url)



def test_alert():
    try:
        # Button Click for JS Alert
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
        time.sleep(3)
        msg1 = driver.switch_to.alert.text
        logging.warning(f' Error: Button click on alert JS is not working properly')
        assert msg1 == "I am a JS Alert"
        print(f'mssssssgggg {msg1}')

        driver.switch_to.alert.accept()
        msg2 = driver.find_element(By.CLASS_NAME, 'result').text
        assert msg2 == "You successfully clicked an alert"
        print(msg2)

        driver.quit()

        # # Button Click for JS Confirm
        # driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
        # time.sleep(3)
        # driver.switch_to.alert.text
        # msg3 =
        # logging.warning(f' Error: Button Click for JS Confirm is not working properly')
        # assert msg3 == "I am a JS Confirm"
        # print(f'mssssssgggg {msg3}')

       # Button Click for JS Confirm
       #  alert = Alert(driver)
       #  driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
       #  time.sleep(3)
       #  driver.switch_to.alert.send_keys("tamar samara")
       #  driver.switch_to.alert.accept()

        # msg3 = driver.switch_to.alert.text
        # logging.warning(f' Error: Button Click for JS Confirm is not working properly')
        # assert msg3 == "I am a JS prompt"
        # print(f'mssssssgggg {msg3}')


    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()
