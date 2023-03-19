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

chrome_options =webdriver.ChromeOptions()
s=Service(ChromeDriverManager().install())
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")

chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=s,options=chrome_options)
wait=WebDriverWait(driver, 60)

driver.get("https://web.whatsapp.com/")
searchbox= wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@title='Search input textbox']")))
searchbox=driver.find_element(By.XPATH,"//div[@title='Search input textbox']")
driver.execute_script("arguments[0].click();", searchbox)
searchbox.send_keys("Whatsqpp Bot")
searchbox.send_keys(Keys.ENTER)
time.sleep(3)
messages=[]
messages1=[]
for i in range(2):
  j=i+1
  
  textcopy=driver.find_elements(By.XPATH,"//span[@class='_11JPr selectable-text copyable-text']")[-j].text
  print(textcopy)
  message_aurthor=driver.find_elements(By.XPATH,"//div[contains(@class,'copyable-text') and contains(@data-pre-plain-text,'')]")[-j].get_attribute('data-pre-plain-text')
  print(message_aurthor)
  messages1.append(message_aurthor)
  messages.append(textcopy)
# time.sleep(200)
message=driver.find_element(By.XPATH,"//div[contains(@class,'fd365im1')]")
message.click()
message.send_keys("HI")
message.send_keys(" @Yoha")
# f=driver.find_element(By.XPATH,"//*[text='Yohannatticot Client France']").click()
message.send_keys(Keys.ENTER)
message.send_keys(Keys.ENTER)
df = pd.DataFrame({'Name of Messenger with time':messages1,'Messages': messages})
df.columns = ['Column 1','Column 2']
df.to_excel('Messages.xlsx', index=False)
time.sleep(1000)