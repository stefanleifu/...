import os.path

from selenium import  webdriver
from time import sleep

from selenium.webdriver.support.select import Select

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/test_alert.html'
        self.driver.get(file_path)

    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert = self.driver.switch_to.alert
        print("Alert content: " + alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('confirm').click()
        confirm = self.driver.switch_to.alert
        print("Confirm content: " + confirm.text)
        sleep(3)
        confirm.dismiss()
        sleep(3)

        self.driver.quit()

    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        print("aaaaaa")
        sleep(3)
        prompt = self.driver.switch_to.alert
        print("aaaaaa")
        sleep(3)
        prompt.accept()
        print("Prompt content: " + prompt)

        self.driver.quit()



if __name__ == '__main__':
    case = TestCase()
    #case.test_alert()
    #case.test_confirm()
    case.test_prompt()

