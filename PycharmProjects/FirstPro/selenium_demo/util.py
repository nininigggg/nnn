from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    sleep(1)

    loc = (By.ID, 'kw')
    loc2 = (By.ID, 'su')

    get_element(driver, *loc).send_keys('selenuim')
    get_element(driver, *loc2).click()

