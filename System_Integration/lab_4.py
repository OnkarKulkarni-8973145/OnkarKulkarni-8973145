# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Steam homepage
driver.get("https://store.steampowered.com/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","store_nav_search_term")
search_bar.send_keys("PUBG")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(3)

# Verifying that the search results page has loaded
# assert "PUBG" in driver.title

# Selecting a laptop from the search results
PUBG_link = driver.find_element("xpath","//a[1]/div[2]/div[1]/span")
PUBG_link.click()

# Waiting for the PUBG details page to load
time.sleep(2)

# clicking play game button
play_game_button = driver.find_element("id","freeGameBtn")
play_game_button.click()

# Waiting for got steam? page to open
time.sleep(3)

# clicking need steam button

need_steam_button = driver.find_element("xpath", "/html/body/div[4]/div/div/div[1]/a[2]/h5")
need_steam_button.click()

# waiting for need steam page to load
time.sleep(2)

# Closing the webdriver
driver.close()
