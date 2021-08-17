from selenium import webdriver

chrome_driver_path = input("Enter chrome driver path: ")
# Download the latest driver from https://chromedriver.chromium.org/ based on your chrome version

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

button = driver.find_element_by_id('bigCookie')
while True:
    button.click()
