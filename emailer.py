from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options
import time
import mysql.connector
import json
class email():
    def send(db):
        username = ""
        password = ""
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver = webdriver.Chrome(executable_path='/Driver/chromedriver',options = option)
        driver.get("https://gmail.com")
        driver.implicitly_wait(5)
        search = driver.find_element_by_xpath("//input[@type='email']")
        search.send_keys(username)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        search = driver.find_element_by_xpath("//input[@type='password']")
        search.send_keys(password)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        total = 0
        emails_sent = 0
        for x in db:
            total +=1
        for i in db:
            search = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
            search.click()
            driver.implicitly_wait(2)
            search = driver.find_element_by_xpath("//textarea[@name='to']")
            search.send_keys(i)
            search = driver.find_element_by_xpath("//input[@name='subjectbox']")
            search.send_keys("Automated Email Testing")
            search = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")
            search.send_keys("Hello all invited users. If you are recieving this message Jaden is running tests")
            search = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
            search.click()
            time.sleep(3)
            emails_sent += 1
            print('%d out of %d emails sent...' %(emails_sent,total))
        driver.close()
        print("Finished sending emails!")