from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd

class WordpressListingLinks:
    data = {}

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def land_required_page(self, my_url):
        self.driver.get(my_url)
        self.driver.implicitly_wait(5)

    def get_links(self, file):
        links = self.driver.find_elements(By.XPATH, '//div[@class="show-img"]/a')
        self.driver.implicitly_wait(5)
        images = self.driver.find_elements(By.XPATH, '//div[@class="show-img"]/a/img')
        self.driver.implicitly_wait(5)
        for l, i  in zip(links, images):
            self.data['Link'] = l.get_attribute('href')
            self.data['Image'] = i.get_attribute('src')
            print("Link: "+str(l.get_attribute('href')))
            print("Image: "+i.get_attribute('src'))
            p = pd.DataFrame([self.data])
            p.to_csv(f"path/{file}.csv", mode='a', encoding='Latin1', header=not
                     os.path.exists(f"path/{file}.csv"), index=False)

    def handle_pagination(self, i):
        next_btn = self.driver.find_element(By.XPATH, f'//span[@data-pageurl="{i}"]')
        self.driver.implicitly_wait(5)
        next_btn.click()


url = str(input("Enter Url: "))
file_name = str(input("Enter File Name: "))
n = int(input("Enter number of pages: "))
bot = WordpressListingLinks()
bot.land_required_page(url)
i = 1
while i <= n:
    try:
        bot.get_links(file_name)
        bot.handle_pagination(i+1)
        i = i + 1
        time.sleep(10)
    except:
        print("Loop Limit Exceed")
        break

