# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the rockstar games homepage
driver.get("https://www.rockstargames.com/")
time.sleep(5)

# clicking three lines button at top left corner
three_lines_button = driver.find_element("xpath", "/html/body/div[1]/div[4]/header/div[1]/button")
three_lines_button.click()
time.sleep(3)

# clicking gtav icon
gtav_button = driver.find_element("xpath", "/html/body/div[1]/div[4]/nav/div[2]/div/ul/li[1]/div/div[2]/div/div[1]/div/a")
gtav_button.click()
time.sleep(3)

# clicking buy now button
buy_now_button = driver.find_element("xpath", "//*[@id='content']/div/div/div[1]/div/div[2]/div[3]/div/a[2]")
buy_now_button.click()
time.sleep(5)

# clicking the select platform button
select_platform_button = driver.find_element("xpath", "//*[@id='main']/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/button")
select_platform_button.click()
time.sleep(3)

# clicking ps5 button
ps5_button = driver.find_element("xpath", "//*[@id='main']/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div[2]/button/div[2]/div/span[1]/a")
ps5_button.click()
time.sleep(3)

# Closing the webdriver
driver.close()
