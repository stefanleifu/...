import os.path

from selenium import  webdriver
from time import sleep

from selenium.webdriver.support.select import Select


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///' + path + '/form3.html'
        self.driver.get(file_path)
    def test_select(self):
        se = self.driver.find_element_by_id('provise')
        select = Select(se)
        # select.select_by_index(2)
        # sleep(2)
        # select.select_by_value('TJ')
        # sleep(2)
        # select.select_by_visible_text('Beijing')
        # sleep(2)

        for i in range(3):
            select.select_by_index(i)
            sleep(2)
        sleep(3)
        select.deselect_all()
        sleep(3)

        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    case.test_select()