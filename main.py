from selenium import webdriver
import os
from login import login


#give file address and remove file name from address
path = os.path.dirname(os.path.abspath(__file__))

address = os.path.join(path, "chromedriver.exe")

driver = webdriver.Chrome(executable_path = address)

#go to instagram
driver.get("https://instagram.com")


login(driver)


