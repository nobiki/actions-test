import os
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# this is sample program
print("Hello")

# grid_host = os.environ.get('GRID_HOST')

if "chrome" == os.environ.get('BROWSER'):
    browser=DesiredCapabilities.CHROME
elif "edge" == os.environ.get('BROWSER'):
    browser=DesiredCapabilities.EDGE
elif "ie" == os.environ.get('BROWSER'):
    browser=DesiredCapabilities.INTERNETEXPLORER
else:
    browser=DesiredCapabilities.FIREFOX

driver = webdriver.Ie(desired_capabilities=browser)
driver.get("https://7me.oji.0j0.jp")
time.sleep(10)
driver.close()
driver.quit()
