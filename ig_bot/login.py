from driver import *


def login(driver):

    display(Image(driver.get_screenshot_as_png()))
    
    if driver.current_url == 'https://www.instagram.com/':
        username = driver.find_element(By.NAME, 'username')
        # password = driver.find_element(By.NAME, 'password')

        print(username)
        # print(password)

driver = initialize('https://www.instagram.com')
login(driver)