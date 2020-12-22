from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
from getpass import getpass

class InstaBot:
    def __init__(self,username,password,post_url,comments):
        PATH = ("C:\Program Files (x86)\chromedriver.exe")
        self.driver = webdriver.Chrome(PATH)
        self.driver.get(post_url)
        time.sleep(2)

        #clicks the popup accept button
        self.driver.switch_to_alert
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        self.driver.switch_to_default_content

        #clicks login button
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button").click()
        time.sleep(2)

        self.login(username, password)
        
        try:
            #clicks save info not now 
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/div/div/div/button"))
            )
            element.click()

            #COMMENTS for ever
            print("Now the bot spams every 4 to 5 minutes the comment that you entered")
    
            while True:
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button").click()
                time.sleep(2)
                self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea").send_keys(comments)
                time.sleep(2)   
                send = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button"))
                )
                send.click()
                
                time.sleep(randint(240,300))
        except:
            self.driver.quit()

    def to_profile(self):
        searchBar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div"))
            )
        searchBar.click()
        time.sleep(2)

        search = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        search.send_keys("@konstantinos_koutsilis")
        search.send_keys(Keys.RETURN)
        time.sleep(2)

        profile = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a"))
        )
        profile.click()
        time.sleep(4)     

    def login(self,username,password):
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        




username = input("Give your instagram username here: " )
password = getpass("Give your instagram password here: ")
post_url = input("Paste the url of the giveaway post here: ")
comments = input("Give the comment that the bot will spam here" )
InstaBot(username,password,post_url,comments)