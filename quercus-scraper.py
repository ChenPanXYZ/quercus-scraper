from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv()

UTORID = os.getenv('UTORID')
PASSWORD = os.getenv('PASSWORD')

chromeOptions = Options()
chromeOptions.headless = True
chromeOptions.add_argument('--no-sandbox')   
browser = webdriver.Chrome(executable_path="./chromedriver", options=chromeOptions)
browser.get("https://q.utoronto.ca/")

print("Loading page...")
print("I am logining...")
browser.find_element_by_id('username').send_keys(UTORID)
browser.find_element_by_id('password').send_keys(PASSWORD)
browser.find_element_by_name('_eventId_proceed').click()
time.sleep(1)
print("Logged in!")
students = []
courseID = ""
for i in range(0, 1000):
    print(i)
    for student in students:
        browser.get("https://q.utoronto.ca/courses/" + courseID +  "/users/" + student + "/usage")
        df = pd.read_html(browser.page_source)[0]
        df.to_excel("./datasets/" + str(i) + "-" + student + ".xlsx")
browser.quit()