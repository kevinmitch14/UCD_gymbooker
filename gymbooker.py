import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
from git import Repo

student_number = 20202928

# Opening log file to log process
file = open("log.txt", "a")

# # Gym booking landing page
url = "https://sisweb.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK"

# Creating Options object for use on EC2 linux machine
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Initialising driver
driver = webdriver.Chrome(options=options)

# Getting landing page URL
driver.get(url)
print("URL found")
file.write("URL FOUND " + str(datetime.now()))

# Screenshot after opening Webpage
driver.save_screenshot("1.png")

# Locate desired session - this corresponds to 7AM
session = driver.find_element_by_xpath('//*[@id="SW300-1|1"]/td[6]/a')
session.click()
print("Clicked session")
file.write("Session clicked " + str(datetime.now()))

# Screenshot after clicking the session.
driver.save_screenshot("2.png")

# Handle cookie popup.
cookie = driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]')
cookie.click()

print("Cookie clicked")
file.write("Cookie clicked " + str(datetime.now()))

enter_student_number = driver.find_element_by_xpath(
    '//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[4]')
enter_student_number.send_keys(student_number)

driver.save_screenshot("3.png")

print("Student number entered and sent.")
file.write("Student number entered " + str(datetime.now()))

confirm_booking = driver.find_element_by_xpath(
    '//*[@id="single-column-content"]/div/div/div/div[2]/div/form/input[5]')
confirm_booking.click()
file.write("Confirm clicked " + str(datetime.now()))

driver.save_screenshot("4.png")

confirm_handler = driver.find_element_by_xpath(
    '//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]')
confirm_handler.click()
file.write("Confirm 2 clicked " + str(datetime.now()))

driver.save_screenshot("5.png")

final_confirm = driver.find_element_by_xpath(
    '//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]')
final_confirm.click()
file.write("Confirm 3 clicked " + str(datetime.now()))

driver.save_screenshot("6.png")

# Getting pwd of file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Performing git actions on file to push to remote Github repository
repository = Repo.init(dir_path)
repository.git.add("--all")
repository.git.commit("-m", "commit message from python script")
origin = repository.remote(name="origin")
origin.push(force=True)
