from time import sleep
from selenium import webdriver
import os


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path1 = os.path.dirname(os.path.abspath(__file__))
        path2 = os.path.abspath(__file__)
        file_path = 'file:///' + path1 + '/forms.html'
        self.driver.get(file_path)

        print("path1: " + path1)
        print("path2: " + path2)
        print("file_path: " + file_path)

    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('admin')
        pwd = self.driver.find_element_by_id('pwd')
        pwd.send_keys('123333')
        sleep(2)
        self.driver.find_element_by_id('submit').click()
        self.driver.switch_to.alert.accept()
        username.clear()
        pwd.clear()

if __name__ == '__main__':
    case = TestCase()
    case.test_login()
