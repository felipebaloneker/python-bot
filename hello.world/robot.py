import time
import os, inspect, sys;
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

try:
    CURRENTDIR = '/Users/hunter/Documents/projects/personal/bots/chromedriver'
    chrome_options = webdriver.ChromeOptions();
    chrome_options.add_argument('--headless');
    chrome_options.add_argument('--no-sandbox');
    chrome_options.add_argument('--mute-audio')
    driver = webdriver.Chrome(CURRENTDIR, chrome_options=chrome_options)

    driver.get("http://www.google.com");
    print(driver.title)
except:
    print("error")

finally:
    driver.close()