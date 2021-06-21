from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def test(self):
        self.driver.get('https://www.google.com/')
        slef.driver.maximize_window()

    def test_prop(self):
        print(self.driver.name) #浏览器名称
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        sleep(1)
        slef.driver.refresh()


        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_prop()