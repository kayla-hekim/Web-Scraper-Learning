# from bs4 import BeautifulSoup
# import requests
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import getpass

browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
page_to_scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.get("http://quotes.toscrape.com")

page_to_scrape.find_element(By.LINK_TEXT, "Login").click()

time.sleep(3)
username = page_to_scrape.find_element(By.ID, "username")
password = page_to_scrape.find_element(By.ID, "password")
username.send_keys("admin")
my_pass = getpass.getpass()
password.send_keys(my_pass)
page_to_scrape.find_element(By.CSS_SELECTOR, "input.btn-primary").click()

quotes = page_to_scrape.find_element(By.CLASS_NAME, "text")
authors = page_to_scrape.find_element(By.CLASS_NAME, "author")

file = open("scraped_quotes2.csv", "w")
writer = csv.writer(file)

writer.writerow(["Quotes", "Authors"])

for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])

file.close()