import os
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Ie("IEDriverServer.exe")
driver.get("https://7me.oji.0j0.jp")
time.sleep(10)
driver.close()
driver.quit()
