from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import ArcGIS
import pandas as pd
import time
import os


class TherapyInColorData:
    data_dict = {}
    #service = Service(path='')
    option = Options()
    geocode = ArcGIS(timeout=10)

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def land_required_page(self, my_url):
        self.driver.get(my_url)
        self.driver.implicitly_wait(10)

    def get_name(self):
        try:
            name = self.driver.find_element(By.XPATH, '//h1').text
            self.driver.implicitly_wait(5)
            print("Name: " + name)
            self.data_dict['Name'] = name
        except:
            self.data_dict['Name'] = 'N/A'

    def get_speciality(self):
        try:
            spec = self.driver.find_element(By.XPATH, '//div[@class="post-meta-left-box"]/p').text
            self.driver.implicitly_wait(5)
            print("Speciality: " + spec)
            self.data_dict['Speciality'] = spec
        except:
            self.data_dict['Speciality'] = 'N/A'

    def treatment_approach(self):
        try:
            condition = self.driver.find_element(By.XPATH,
                                                 '//div[@class="features-listing extra-fields"]/ul/li/strong').text
            self.driver.implicitly_wait(5)
            if condition == 'Approach to treatment:':
                try:
                    approach = self.driver.find_element(By.XPATH,
                                                        '//div[@class="features-listing extra-fields"]/ul/li/span').text
                    self.driver.implicitly_wait(5)
                    print("Treatment Approach: " + approach)
                    self.data_dict['Treatment Approach'] = approach
                except:
                    self.data_dict['Treatment Approach'] = 'N/A'
            else:
                try:
                    approach = self.driver.find_element(By.XPATH,
                                                        '//div[@class="features-listing extra-fields"]/ul/li[2]/span').text
                    self.driver.implicitly_wait(5)
                    print("Treatment Approach: " + approach)
                    self.data_dict['Treatment Approach'] = approach
                except:
                    self.data_dict['Treatment Approach'] = 'N/A'
        except:
            self.data_dict['Treatment Approach'] = 'N/A'


    def get_insurance_accepted(self):
        try:
            test = self.driver.find_element(By.XPATH, '//div[@class="features-listing extra-fields"]/ul/li[3]/strong').text
            self.driver.implicitly_wait(5)

            if test == 'Insurance Accepted:':
                insure = self.driver.find_element(By.XPATH, '//div[@class="features-listing extra-fields"]/ul/li[3]/span').text
                self.driver.implicitly_wait(5)
                print("Insurance Accepted: " + insure)
                self.data_dict['Insurance Accepted'] = insure
            else:
                self.data_dict['Insurance Accepted'] = 'N/A'
        except:
            self.data_dict['Insurance Accepted'] = 'N/A'


    def get_discription(self):
        try:
            discript = self.driver.find_element(By.XPATH, '//div[@class="post-detail-content"]').text
            self.driver.implicitly_wait(5)
            print("Discription: " + discript.strip())
            self.data_dict['Discription'] = discript.strip()
        except:
            self.data_dict['Discription'] = 'N/A'

    def get_ratting(self):
        try:
            rate = self.driver.find_element(By.XPATH, '//span[@class="rate lp-rate-good"]').text
            self.driver.implicitly_wait(5)
            print("Ratting: "+rate.strip())
            self.data_dict['Ratting'] = rate.strip()
        except:
            self.data_dict['Ratting'] = 'N/A'


    def get_address(self):
        try:
            address = self.driver.find_element(By.XPATH, '//li[@class="lp-details-address"]/a/span[2]').text
            self.driver.implicitly_wait(5)
            print("Address: " + address)
            self.data_dict['Address'] = address
            coordinates = self.geocode.geocode(address)
            print("Latitude: " + str(coordinates.latitude))
            print("Longitude: " + str(coordinates.longitude))
            self.data_dict['Latitude'] = str(coordinates.latitude)
            self.data_dict['Longitude'] = str(coordinates.longitude)
        except:
            self.data_dict['Address'] = 'N/A'
            self.data_dict['Latitude'] = 'N/A'
            self.data_dict['Longitude'] = 'N/A'

    def get_phone_number(self):
        try:
            phone = self.driver.find_element(By.XPATH, '//li[@class="lp-listing-phone"]/a/span[2]').text
            self.driver.implicitly_wait(5)
            print("Phone # " + phone)
            self.data_dict['Phone'] = phone
        except:
            self.data_dict['Phone'] = 'N/A'

    def get_website(self):
        try:
            web = self.driver.find_element(By.XPATH, '//li[@class="lp-user-web"]/a/span[2]').text
            self.driver.implicitly_wait(5)
            print("Website Address: " + web)
            self.data_dict['Website Address'] = web
        except:
            self.data_dict['Website Address'] = 'N/A'

    def get_socail_links(self):
        try:
            fb = self.driver.find_element(By.XPATH, '//li[@class="lp-fb"]/a').get_attribute('href')
            self.driver.implicitly_wait(5)
            print("Facebook Link: " + fb)
            self.data_dict['Facebook'] = fb
        except:
            self.data_dict['Facebook'] = 'N/A'

        try:
            tw = self.driver.find_element(By.XPATH, '//li[@class="lp-tw"]/a').get_attribute('href')
            self.driver.implicitly_wait(5)
            print("Twitter Link: " + tw)
            self.data_dict['Twitter'] = tw
        except:
            self.data_dict['Twitter'] = 'N/A'

        try:
            ins = self.driver.find_element(By.XPATH, '//li[@class="lp-li"]/a').get_attribute('href')
            self.driver.implicitly_wait(5)
            print("Instagram Link: " + ins)
            self.data_dict['Instagram'] = ins
        except:
            self.data_dict['Instagram'] = 'N/A'

    def get_timings(self):
        my_time = []
        try:
            time_open = self.driver.find_element(By.XPATH, '//div[@class="open-hours"]/div/div/a')
            self.driver.implicitly_wait(5)
            time_open.click()
            my_t = self.driver.find_elements(By.XPATH, '//li[@class="clearfix lpdoubltimes"]')
            self.driver.implicitly_wait(5)
            for m in my_t:
                time.sleep(1)
                my_time.append(m.text)

            print(my_time)
            self.data_dict['Timings'] = str(my_time)
        except:
            self.data_dict['Timings'] = 'N/A'
        my_time.clear()


    def get_url(self, type, img):
        self.data_dict['Listing Type'] = type.title()
        self.data_dict['Profile Image'] = img
        self.data_dict['Listing Url'] = self.driver.current_url

    def get_youtube_link(self):
        try:
            you = self.driver.find_element(By.XPATH, '//a[@class="watch-video popup-youtube"]').get_attribute('href')
            self.driver.implicitly_wait(6)
            print("Youtube Link: "+str(you))
            self.data_dict['YouTube Link'] = you
        except:
            self.data_dict['YouTube Link'] = 'N/A'

    def move_into_file(self, file):
        p = pd.DataFrame([self.data_dict])
        p.to_csv(f"path/{file}.csv", mode='a', header=not
            os.path.exists(f"path/{file}.csv"), index=False)

        p.to_csv(f"path/combine.csv", mode='a',  header=not
            os.path.exists(f"path/combine.csv"), index=False)


file_list = [
    'Licensed Clinical Social Worker',
    'Licensed Drug and Alcohol Counselor',
    'Life coach',
    'Marriage and family therapist',
    'pastoral Councelor',
    'spirtual therapist',
    'sex therapist',
    'psychotherapist intern',
    'psychotherapist',
    'psychologist'
]
bot = TherapyInColorData()
links = []
images = []
for f in file_list:
    with open(f"path/{f}.csv", encoding='Latin1') as file:
        for fi in file:
            # link = fi.split(',')
            # links.append(link[0])
            # images.append(link[-1])
            links.append(fi)
            images.append('hi')
    for l, i in zip(links, images):
        bot.land_required_page(l)
        bot.get_name()
        bot.get_speciality()
        bot.treatment_approach()
        bot.get_insurance_accepted()
        bot.get_discription()
        bot.get_ratting()
        bot.get_address()
        bot.get_phone_number()
        bot.get_website()
        bot.get_socail_links()
        bot.get_timings()
        bot.get_youtube_link()
        bot.get_url(f, i)
        bot.move_into_file(f)
    links.clear()


