from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# student_number = 20202920

# driver = webdriver.Chrome()
# driver.get('https://sisweb.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK')

# message = driver.find_element_by_css_selector("h1").text
# print(message)

# session = driver.find_element_by_xpath('//*[@id="SW300-1|3"]/td[6]/a')
# session.click()

# cookie = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
# cookie.click()

# print("Cookie clicked")

# enter_student_number = driver.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[4]')
# enter_student_number.send_keys(student_number)


# confirm_booking = driver.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[5]')
# confirm_booking.click()

# confirm_message = driver.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div').text
# print(confirm_message)

# confirm2 = driver.find_element_by_xpath('//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]')
# confirm2.click()


import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)