from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://www.google.com/')
        self.driver.find_element_by_class_name('gLFyf').send_keys("editionrecord")
        sleep(1)
        self.driver.find_element_by_class_name('gLFyf').send_keys(Keys.ENTER)
        sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test()