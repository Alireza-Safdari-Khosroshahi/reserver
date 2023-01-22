from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from Mail import sendMail


def scraper():
    driver = webdriver.Firefox()
    driver.get("https://ir-appointment.visametric.com/en")
    time.sleep(3)
    assert "Visametric" in driver.title
    elem = driver.find_element_by_name('schengenBtn')
    elem.click()
    time.sleep(3)
    elem = driver.find_element_by_id('result0')
    elem.click()
    time.sleep(1)
    elem = driver.find_element_by_id('result1')
    elem.click()
    elem = driver.find_element_by_id('btnSubmit')
    elem.click()
    time.sleep(3)
    elem = driver.find_element_by_id('city')
    select = Select(elem)
    select.select_by_value('2')
    elem = driver.find_element_by_id('office')
    select = Select(elem)
    select.select_by_value('1')
    elem = driver.find_element_by_id('officetype')
    select = Select(elem)
    select.select_by_value('1')
    elem = driver.find_element_by_id('totalPerson')
    select = Select(elem)
    select.select_by_value('1')
    elem = driver.find_element_by_id('availableDayInfo')
    print(elem.text)
    if elem.text != "There isn't any available date.":
        sendMail()
    driver.close()

if __name__ == "__main__":
    while True:
        scraper()
        time.sleep(60)