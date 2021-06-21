from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    sleep(1)

    loc = (By.CLASS_NAME,'gLFyf')

    get_element(driver, *loc).send_keys('editionrecord')
    sleep(1)
    get_element(driver, *loc).send_keys(Keys.ENTER)
    sleep(2)


