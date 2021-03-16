#selenium
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

#chromedriver
from webdriver_manager.chrome import ChromeDriverManager

import time
from colorama import init, Fore, Back, Style
from datetime import datetime
from time import gmtime, strftime

import pyttsx3
engine = pyttsx3.init()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument('log-level=3')

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

init(convert=True)

def getStat(url):
    driver.get(url)

    pageText = driver.find_element_by_tag_name('body')

    pageText = pageText.text.split('\n')

    isSoldOut = False

    for i in pageText:
        if i == "Sold out":
            isSoldOut = True
        elif i == "Delivery" or i == "Pick up" or i == "In Stock":
            isSoldOut = False
        
    return(isSoldOut)

def logInStock(name,platform,price):
    f = open('log.txt', "a")
    f.write(platform+","+price+","+name+","+datetime.now().strftime('%m/%d %H:%M EST')+"\n")
    f.close()

def mainLoop(url,platform,price,name):

    wasInStock = False

    while True:
        print(Fore.CYAN + platform+ name)
        print(Fore.WHITE +"Checking...")
        isSoldOut = getStat(url)
        if isSoldOut == False:
            print(Fore.CYAN + platform + name)
            print(Fore.GREEN +"In Stock")
            engine.say(platform+name+"In Stock for"+price)
            engine.runAndWait()
            if wasInStock == False:
                logInStock(name,platform,price)
                wasInStock = True
        else:
            print(Fore.CYAN + platform +name)
            print(Fore.RED +"Out Of Stock")
            wasInStock = False

        time.sleep(1.5)