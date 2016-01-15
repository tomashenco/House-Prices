from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import requests


def read_page(url):
    r = requests.get(url)
    print r.text



def web_seeker(locations):
    # Create driver
    driver = webdriver.Chrome()

    # Execute for each location
    for city in locations:
        # Open website
        driver.get('http://www.rightmove.co.uk/property-for-sale./find.html')
        # Check if opened
        assert "UK's number one" in driver.title

        # Select city in search box and proceed
        search_form = driver.find_element_by_id('searchLocation')
        search_form.send_keys(city)
        search_form.send_keys(Keys.RETURN)

        # Select search parameters
        radius = Select(driver.find_element_by_id('radius'))
        radius.select_by_index(10)  # 40 miles
        min_price = Select(driver.find_element_by_id('minPrice'))
        min_price.select_by_index(6)  # 100k
        max_price = Select(driver.find_element_by_id('maxPrice'))
        max_price.select_by_index(27)  # 400k
        property_type = Select(driver.find_element_by_id('displayPropertyType'))
        property_type.select_by_index(1)  # houses only
        added = Select(driver.find_element_by_id('maxDaysSinceAdded'))
        added.select_by_index(1)  # last 24 hours

        # Submit search paremeters
        submit_button = driver.find_element_by_id('submit')
        submit_button.click()

        # Look at all pages but now more than 100
        index = 0
        while index < 2:
            # Look for all offers and get URLs
            links = driver.find_elements_by_partial_link_text('More')
            for link in links:
                # Pass URL to reader
                read_page(link.get_attribute('href'))

            # Next page
            try:
                next_url = driver.find_element_by_partial_link_text('next')
            except NoSuchElementException:
                break
            index += 1
            driver.get(next_url.get_attribute('href'))

