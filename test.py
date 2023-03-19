from selenium import webdriver
import requests
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# chrome_options.add_experimental_option("debuggerAddress", f"localhost:{9222}")

# chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options,service=s)
driver.get("https://web.whatsapp.com/")
time.sleep(1000)