from selenium import webdriver
from time import sleep

def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('taylorswift')
    sleep(2)
    driver.find_element_by_id('su').click()
    sleep(3)
    driver.quit()

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

        def test(self):
            self.get('http://www.baidu.com')
            sleep(2)
            self.find_element_by_id('kw').send_keys('taylorswift')
            sleep(2)
            self.find_element_by_id('su').click()
            sleep(3)
            self.driver.quit()

def test():
    import  subprocess
    p = subprocess.Popen("chromedriver")
    p.communicate()

if __name__ == '__main__':
    case = TestCase()
    case.test()