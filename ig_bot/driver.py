import sys, time, os
from datetime import date, datetime
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from IPython.display import Image, display


opts = open(os.path.join('options.txt'), 'r')

for opt in opts:
    print(opt.strip())

def initialize(init_page):
    options = webdriver.ChromeOptions()
    
    for opt in opts:
        options.add_argument(opt.strip())
    
    driver = webdriver.Chrome(options=options, executable_path='chromedriver')
    driver.get(init_page)
    display(Image(driver.get_screenshot_as_png()))
    

initialize('https://www.instagram.com')