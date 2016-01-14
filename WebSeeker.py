from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests

def read_page(url):
    pass



def web_seeker(locations):
    # Create driver
    driver = webdriver.Chrome()

    # Execute for each location
    for city in locations:
        # Open website
        driver.get('http://www.rightmove.co.uk/property-for-sale./find.html')
        # Check if opened
        assert "UK's number one" in driver.title

        search_form = driver.find_element_by_id('searchLocation')
        search_form.send_keys(city)
        search_form.send_keys(Keys.RETURN)

        radius = Select(driver.find_element_by_id('radius'))
        radius.select_by_index(10)  # 40 miles
        max_price = Select(driver.find_element_by_id('maxPrice'))
        max_price.select_by_index(32)  # 400k
        property_type = Select(driver.find_element_by_id('displayPropertyType'))
        property_type.select_by_index(1)  # houses only
        added = Select(driver.find_element_by_id('maxDaysSinceAdded'))
        added.select_by_index(1)  # last 24 hours

        find_button = driver.find_element_by_id('submit')
        find_button.click()

        link = driver.find_element_by_xpath('//*[@href]')
        print link.get_attribute('href')
