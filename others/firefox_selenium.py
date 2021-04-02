from selenium import webdriver

# variable du driver
driver = webdriver.Firefox(executable_path = "/home/leo/snap/geckodriver")
driver.get("https://cp-algorithms.com/")
