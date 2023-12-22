from selenium import webdriver
driver_location = "/snap/bin/chromium.chromedriver"
binary_location = "/usr/bin/chromium-browser"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = binary_location
driver = webdriver.Chrome(executable_path=driver_location, options=chrome_options)
driver.get("https://www.google.co.in/")
print(driver.page_source.encode('utf-8'))
driver.quit()
