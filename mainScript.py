#selenium
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

#chromedriver
from webdriver_manager.chrome import ChromeDriverManager

#time
import time

#colored print line
from colorama import init, Fore, Back, Style
init(convert=True)

#date and time
from datetime import datetime
from time import gmtime, strftime

#text to speech
import pyttsx3
engine = pyttsx3.init()

#plays sound
from playsound import playsound

#setting up chrome options
options = Options()
options.add_argument('--headless')  #headless mode
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument('log-level=3')   #stops nitifications from coming through


#defining our driver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


#gets in stock or not in stock status
def getStat(url):

    #go to page
    driver.get(url)

    #get all text from body
    pageText = driver.find_element_by_tag_name('body')

    #plit all texta at newline
    pageText = pageText.text.split('\n')

    #defining in stock
    isSoldOut = False

    #checking for "in stock" or "out of stock" text on page
    for i in pageText:
        if i == "Sold out":
            isSoldOut = True
        elif i == "Delivery" or i == "Pick up" or i == "In Stock":
            isSoldOut = False

        #return result 
    return(isSoldOut)

#log when in stock
def logInStock(name,platform,price):
    f = open('log.txt', "a")
    f.write(platform+","+price+","+name+","+datetime.now().strftime('%m/%d %H:%M EST')+"\n")
    f.close()


def mainLoop(url,platform,price,name):

    #defining var
    wasInStock = False

    #loops forever
    while True:

        #print "checking"
        print(Fore.CYAN + platform+ name)
        print(Fore.WHITE +"Checking...")

        #get status
        isSoldOut = getStat(url)

        #if its in stock
        if isSoldOut == False:
            #print in stock
            print(Fore.CYAN + platform + name)
            print(Fore.GREEN +"In Stock")

            #tts say that its in stock
            engine.say(platform+name+"In Stock for"+price)
            engine.runAndWait()

            #play alarm sound
            playsound('alarm.mp3')

            #if it was in stock then dont log again
            if wasInStock == False:
                logInStock(name,platform,price)
                wasInStock = True

        else:#if its out of stock

            #print out of stock
            print(Fore.CYAN + platform +name)
            print(Fore.RED +"Out Of Stock")
            wasInStock = False

        #wait
        time.sleep(1.5)