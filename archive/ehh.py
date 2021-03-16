#selenium
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

#chromedriver
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://bestbuy.com/login")

def login():
    
    user = "thisisnotabotdontworry@gmail.com"
    passoword = "Thisisnotabot1"

    driver.find_element_by_xpath(r"/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[1]/div/input").send_keys(user)

    
    driver.find_element_by_xpath(r"/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[2]/div/div/input").send_keys(passoword)


    driver.find_element_by_xpath(r"/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[4]/button").click()

    driver.find_element_by_xpath(r"/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/div/label/div/div/input").click()


def mainLoop():
    driver.get('https://www.bestbuy.com/site/bald-dvd-2005/18072318.p?skuId=18072318')

    pageText = driver.find_element_by_tag_name('body')

    pageText = pageText.text.split('\n')

    isSoldOut = False

    for i in pageText:
        if i == "Sold Out":
            isSoldOut = True
        
    if isSoldOut == False:
        driver.find_element_by_xpath(r"/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[5]/div[1]/div/div/div/button").click()

def checkOut():

    name = "Fat"
    lastName = "Boy"
    adress = "123 white perosn lane"
    city = " oralndo"
    phonenumber = "8474747474"
    zipcode = "1732"
    state = "CA"


    #go to cart and checkout
    driver.get("https://bestbuy.com/cart")
    driver.find_element_by_id("consolidatedAddresses.ui_address_2.firstName").click()

    #name
    driver.find_element_by_xpath(r"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[1]/label/div/input").send_keys(name)

    #last name
    driver.find_element_by_xpath(r"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[2]/label/div/input").send_keys(lastName)

    #adress
    driver.find_element_by_xpath(r"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/div/input").send_keys(adress)

    #city
    driver.find_element_by_xpath(r"s/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[5]/div/div[1]/label/div/input").send_keys(city)

    #phone number
    driver.find_element_by_xpath(r"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/section/div[3]/label/div/input").send_keys(phonenumber)

    #zip code
    driver.find_element_by_xpath(r"/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[6]/div/div[1]/label/div/input").send_keys(zipcode)

    #selecting all properties
    selectProperty = Select(driver.find_element_by_id('property_DropDownList'))
    selectProperty.select_by_visible_text("All Properties")

login()
time.sleep(2)
mainLoop()
time.sleep(2)
checkOut()

#while "poop" != "pee":
    #mainLoop()
    #time.sleep(1000)

