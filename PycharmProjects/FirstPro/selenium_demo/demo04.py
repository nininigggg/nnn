from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# webelement属性和方法
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element(By.ID, 't1')
        print(type(e))
        print(e.id)
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)

        self.driver.quit()

    def test_webelement_method(self):
        e = self.driver.find_element(By.ID, 't1')
        e.send_keys('hello word')
        sleep(2)
        e.clear()

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))

        self.driver.quit()

    def test_method2(self):
        form_elemtnt = self.driver.find_element(By.XPATH, '/html/body/form[1]')
        form_elemtnt.find_element(By.ID, 't1').send_keys('balabala')
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case = TestCase()
    # case.test_webelement_prop()
    # case.test_webelement_method()
    case.test_method2()