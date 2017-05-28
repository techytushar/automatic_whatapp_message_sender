from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

message = input("Enter the message - ")
times = int(input("Number of messages -") )
driver= webdriver.Chrome('F:\\python projects\\selenium web\\chromedriver.exe')
driver.set_page_load_timeout(30)
driver.maximize_window()
driver.get('https://web.whatsapp.com')
driver.implicitly_wait(10)

print("\n")
a=1
path = '//*[@id="pane-side"]/div/div/div/div['+str(a)+']/div/div/div[2]/div[1]/div[1]/span'
title = driver.find_elements_by_xpath(path)
while(len(title)):
    print("Press "+str(a)+" for "+title[0].text + "\n")
    a=a+1
    path= '//*[@id="pane-side"]/div/div/div/div['+str(a)+']/div/div/div[2]/div[1]/div[1]/span'
    title = driver.find_elements_by_xpath(path)

head = input("Response - ")

driver.find_element_by_xpath('//*[@id="pane-side"]/div/div/div/div['+head+']/div/div/div[2]/div[1]/div[1]/span').click()
for i in range(0,times):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(message)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/button').click()

time.sleep(4)
driver.quit()
