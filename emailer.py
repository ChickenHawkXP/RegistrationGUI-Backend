from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import options
import time
import mysql.connector
import json
class email():
    with open("config.json","r") as json_read:
        data = json.load(json_read)
    try:
        database = mysql.connector.connect(host = data['host'],
                                            user = data['user'],
                                            password = data['password'],
                                            database = data['database'],
                                            auth_plugin = data['auth_plugin'])
    except:
        print('Could not make connection with database!')
    cursor = database.cursor()
    username = ""
    password = ""
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(chrome_options=option)
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
    cursor.execute("SELECT `EMAIL` FROM `information`")
    for i in cursor:
        search = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
        search.click()
        search = driver.find_element_by_xpath("//textarea[@name='to']")
        search.send_keys(i)
        search = driver.find_element_by_xpath("//input[@name='subjectbox']")
        search.send_keys("Automated Email Testing")
        search = driver.find_element_by_xpath("//div[@class='Am Al editable LW-avf tS-tW']")
        search.send_keys("Hello all invited users. If you are recieving this message Jaden is running tests")
        search = driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
        search.click()
        time.sleep(3)