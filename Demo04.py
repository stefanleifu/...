from time import sleep
from selenium import webdriver

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        #self.driver.get('http://www.sahitest.com/demo/linkTest.htm')
        self.driver.get('http://www.baidu.com/')

    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.text)
        print(e.rect)
        sleep(3)

    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello world')
        sleep(2)
        e.clear()

        print("Type:" + e.get_attribute('type'))
        print("name:" + e.get_attribute('name'))
        print("value:" + e.get_attribute('value'))
        print("css:" + e.value_of_css_property('color'))
        print("font:" + e.value_of_css_property('font'))
        sleep(2)
        e.clear()
        self.driver.quit()

    def test_windows(self):
        news = self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles

        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)


if __name__ == '__main__':
    case = TestCase()
    #case.test_webelement_prop()
    #case.test_webelement_method()
    case.test_windows()




