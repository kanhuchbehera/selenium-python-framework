from selenium import webdriver

def start_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver