import sys, time, os
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from IPython.display import Image, display
from webdriver_manager.chrome import ChromeDriverManager


opts = open('ig_bot/options.txt', 'r')

def initialize(init_page):
    options = webdriver.ChromeOptions()
    
    for opt in opts:
        options.add_argument(opt.strip())
    
    driver = webdriver.Chrome(options=options, executable_path='chromedriver')
    driver.get(init_page)

    return driver