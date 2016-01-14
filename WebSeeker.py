from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://www.rightmove.co.uk/property-for-sale./find.html')
assert "UK's number one" in driver.title
search_form = driver.find_element_by_id('searchLocation')
search_form.send_keys('York')
search_form.send_keys(Keys.RETURN)

radius = Select(driver.find_element_by_id('radius'))
radius.select_by_index(10)  # 40 miles
radius = Select(driver.find_element_by_id('maxPrice'))
radius.select_by_index(32)  # 400k
radius = Select(driver.find_element_by_id('displayPropertyType'))
radius.select_by_index(1)  # houses only
radius = Select(driver.find_element_by_id('maxDaysSinceAdded'))
radius.select_by_index(1)  # last 24 hours

find_button = driver.find_element_by_id('submit')
find_button.click()

per_page = Select(driver.find_element_by_id('numberOfPropertiesPerPage'))
per_page.select_by_index(2)  # 50 results per page