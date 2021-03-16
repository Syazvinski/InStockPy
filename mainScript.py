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

#gets in stock or not in stock status
def getStat(url,inStockKeywords,outStockKeywords):

    try:
        #go to page
        driver.get(url)
    except:
                print(Fore.RED+"FATAL PROXY ERROR")
                
                options = Options()
                options.add_argument('--headless')  #headless mode
                options.add_argument('--disable-gpu')  # Last I checked this was necessary.
                options.add_argument('log-level=3')   #stops nitifications from coming through

                #defining our driver
                driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

                #go to page
                driver.get(url)

    #get all text from body
    pageText = driver.find_element_by_tag_name('body').text.lower().split('\n')

    #defining in stock
    isSoldOut = False

    #checking for "in stock" or "out of stock" text on page
    for i in pageText:
        for x in outStockKeywords:
            if x == i:
                isSoldOut = True
        for z in inStockKeywords:
            if z == i:
                isSoldOut = False

        #return result 
    return(isSoldOut)

#log when in stock
def logInStock(name,platform,price):
    f = open('log.txt', "a")
    f.write(platform+","+price+","+name+","+datetime.now().strftime('%m/%d %H:%M EST')+"\n")
    f.close()


def mainLoop(url,platform,price,name,inStockKeywords,outStockKeywords,useProxys):
    global driver

    #defining var
    wasInStock = False

    #amount of runs and index
    runs = 0
    m = 0
    i = 0
    
    #loops forever
    while True:
        

        #determines weather to use proxy and cyles through them if so.
        if useProxys == True:

            #defining proxy list
            proxys = []

            #open and store log file
            with open('proxys.txt') as f:
                for line in f:
                    proxys.append(line)

            #gets length of proxys
            amountOfProxys = len(proxys)
            
            #checking if 3 uses have passed
            if m == 3:
                m = 0
                i += 1
            else:
                m += 1

            #if end of list reached restart
            if runs == amountOfProxys:
                i = 0
                
            #settting proxy to i
            PROXY = proxys[i]

            #adding use proxy to chrome options
            options.add_argument('--proxy-server=%s' % PROXY)#adds use proxy argument to options
            
            #defining our driver
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
            
                
        else:
            #defining our driver
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


        #print "checking"
        print(Fore.CYAN + platform+ name)
        print(Fore.WHITE +"Checking...")

        #get status
        isSoldOut = getStat(url,inStockKeywords,outStockKeywords)

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

        #close driver
        driver.close()

        #wait
        time.sleep(1.5)