

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import wget
import os
from time import sleep





class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path='geckodriver-v0.31.0-linux64/geckodriver')

    def login(self):
        bot = self.bot
        print('---------- Logging In ----------')
        bot.get("https://www.instagram.com/")
        sleep(3)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        sleep(5)
        bot.find_element_by_xpath("//button[@type='submit']").click()
        sleep(5)
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/section[1]/main[1]/div[1]/div[1]/div[1]/div[1]/button[1]'))).click()
        sleep(5)
        WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'))).click()
        sleep(5)
        print("Logged in")

    def like_photo(self, hashtag, amount):
        bot = self.bot
        print('---------- Liking Photos ----------')
        pages = []
        bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        sleep(5)
        while len(pages) < amount:
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(10)
            hrefs = bot.find_elements_by_tag_name('a')
            media_hrefs = [elem.get_attribute('href') for elem in hrefs]
            for href in media_hrefs:
                if 'https://www.instagram.com/p/' in href and href not in pages:
                    pages.append(href)
            sleep(5)
            if len(pages) == amount:
                break
            pages = pages[:amount]
        #print(pages)
        print('++++++++++++ number of images to like is ' + str(len(pages)) + ' ++++++++++++')
        for page in pages:
            bot.get(page)
            sleep(5)
            try:
                WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_abm0 _abm1"))).click()
                sleep(5)
            except Exception as e:
                print(e)
                print("Already liked")
                sleep(5)
            

        
            

            
            
                              

            
        

