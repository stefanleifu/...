from selenium import webdriver
from time import sleep
'''
driver = webdriver.Chrome()
driver.get('http://baidu.com')
driver.maximize_window()
sleep(2)

element = driver.find_element_by_id('kw')
element.send_keys('selenium')
print(type(element))
driver.find_element_by_id('su').click()
sleep(3)
driver.quit()
'''
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(2)
    def test_id(self):
        element = self.driver.find_element_by_id('kw')
        element.send_keys('selenium')
        print(type(element))

        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_id()