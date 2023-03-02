from time import sleep
from selenium import webdriver

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(2)
    def test_prop(self):
        # 浏览器名称
        print(self.driver.name)
        # 当前url
        print(self.driver.current_url)
        sleep(3)
        #self.dirver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.back()
        sleep(3)
        self.driver.refresh()
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    #case.test_prop()
    case.test_method()









