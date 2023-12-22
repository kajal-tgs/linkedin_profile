from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


chrome_options = ChromeOptions()
chrome_options.add_extension('Data Scraper .crx')

driver = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
driver.get('https://www.google.co.in/')
driver.quit()
