import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = 'http://the-internet.herokuapp.com/javascript_alerts'
driver.get(url)


#test

@pytest.mark.passed
def test_Button_click_for_JS_Alert():
    '''
    Check Button click on alert JS
    passed
    '''

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button').click()
        time.sleep(3)

        msg1 = driver.switch_to.alert.text
        logging.warning(f' Error: Button click on alert JS is not working properly')
        assert msg1 == "I am a JS Alert"

        driver.switch_to.alert.accept()
        time.sleep(3)
        msg2 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error in msg 2')
        assert msg2 == "You successfully clicked an alert"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()


@pytest.mark.passed
def test_Button_Click_for_JS_Confirm_ok():
    # Button Click for JS Confirm

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
        time.sleep(3)

        msg3 = driver.switch_to.alert.text
        logging.warning(f' Error: Button Click for JS Confirm is not working properly')
        assert msg3 == "I am a JS Confirm"

        driver.switch_to.alert.accept()
        time.sleep(3)
        msg4 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error in msg 4')
        assert msg4 == "You clicked: Ok"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()


@pytest.mark.passed
def test_Button_Click_for_JS_Confirm_Cancel():
    '''
    Button Click for JS Confirm, without typing inside the text box, and click Cancel
    passed
    '''

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button').click()
        time.sleep(3)

        msg3 = driver.switch_to.alert.text
        logging.warning(f' Error: Button Click for JS Confirm is not working properly')
        assert msg3 == "I am a JS Confirm"

        driver.switch_to.alert.dismiss()
        time.sleep(3)
        msg4 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error in msg 4')
        assert msg4 == "You clicked: Cancel"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()


@pytest.mark.passed
def test_Button_Click_for_JS_Prompt_empty_ok():
    '''
    Button Click for JS Confirm, without typing inside the text box, and click OK
    passed
    '''

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
        time.sleep(3)

        msg5 = driver.switch_to.alert.text
        logging.warning(f' Error: Button Click for JS prompt is not working properly')
        assert msg5 == "I am a JS prompt"

        driver.switch_to.alert.accept()
        time.sleep(3)
        msg6 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error output, "You entered:"')
        assert msg6 == "You entered:"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()


@pytest.mark.passed
def test_Button_Click_for_JS_Prompt_empty_Cancel():
    '''
    Button Click for JS Confirm, without typing inside the text box, and click Cancel
    passed
    '''

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
        time.sleep(3)

        msg5 = driver.switch_to.alert.text
        logging.warning(f' Error: Button Click for JS prompt is not working properly')
        assert msg5 == "I am a JS prompt"

        driver.switch_to.alert.dismiss()
        time.sleep(3)
        msg6 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error output, "You entered: null"')
        assert msg6 == "You entered: null"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()


@pytest.mark.passed
def test_Button_Click_for_JS_Prompt_write_OK():
    '''
    Button Click for JS Confirm, without typing inside the text box, and click OK
    passed
    '''

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
        time.sleep(3)

        msg5 = driver.switch_to.alert.text
        logging.warning(f' Error: Button Click for JS prompt is not working properly')
        assert msg5 == "I am a JS prompt"

        driver.switch_to.alert.send_keys("tamar samara")
        time.sleep(3)
        driver.switch_to.alert.accept()
        msg6 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error output, "You entered: tamar samara"')
        assert msg6 == "You entered: tamar samara"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()


def test_Button_Click_for_JS_Prompt_write_Cancel():
    '''
    Button Click for JS Confirm, without typing inside the text box, and click OK
    passed
    '''

    try:
        driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
        time.sleep(3)

        msg5 = driver.switch_to.alert.text
        logging.warning(f' Error: Button Click for JS prompt is not working properly')
        assert msg5 == "I am a JS prompt"

        driver.switch_to.alert.send_keys("tamar samara")
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        msg6 = driver.find_element(By.ID, 'result').text
        logging.warning(f' Error output, "You entered: null"')
        assert msg6 == "You entered: null"
        time.sleep(2)

    except Exception as e:
        print("error in code: {}".format(e))
        exit(0)

    finally:
        print("exit")
        time.sleep(5)
        driver.quit()
