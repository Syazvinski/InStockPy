#selenium
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

#chromedriver
from webdriver_manager.chrome import ChromeDriverManager

#colored print line
from colorama import init, Fore, Back, Style

#date and time
from datetime import datetime
from time import gmtime, strftime

#plays sound
from playsound import playsound

#for system os identification
from sys import platform

#for file paht handling
import os

if platform == "linux" or platform == "linux2":
    #linux
    pass
elif platform == "darwin":
    #mac
    pass
elif platform == "win32":
    init(convert=True)

class main:

    def __init__(self):
        #setting up chrome options
        self.options = Options()
        self.options.add_argument('log-level=3')   #stops nitifications from coming through

        #amount of runs and index
        self.runs = 0
        self.m = 0
        self.i = 0

        #setting bools
        self.debugBool = False

        self.proxyBool = False  

        self.headBool = False

        self.audioCueBool = False

    def debug(self,debugBool):
        self.debugBool = debugBool

    def headless(self,headBool):
        self.headBool = headBool
        if (self.headBool == True):

            #debug
            if (self.debugBool == True):
                print(Fore.YELLOW+'Headless Enabled'+Fore.WHITE)

            #adding args for headless chrome
            self.options.add_argument('--headless')  #headless mode
            self.options.add_argument('--disable-gpu')  # Last I checked this was necessary.

            #defining our driver
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)

    def useProxy(self,proxyBool,proxyPath,amntReuse):

        self.proxyBool = proxyBool

        

        if (proxyBool == True):

            #debug
            if (self.debugBool == True):
                print(Fore.YELLOW+'Proxys Enabled'+Fore.WHITE)

            #defining proxy list
            self.proxys = []

            #open and store log file
            with open(proxyPath) as f:
                for line in f:
                    self.proxys.append(line)

            #gets length of proxys
            amountOfProxys = len(self.proxys)
            
            #checking if uses have passed
            if self.m == amntReuse:
                self.m = 0
                self.i += 1
            else:
                self.m += 1

            #if end of list reached restart
            if self.runs == amountOfProxys:
                self.i = 0
            


            #settting proxy to i
            PROXY = self.proxys[self.i]

            #debug
            if (self.debugBool == True):
                print(Fore.YELLOW+"CONNECTING TO PROXY"+" "+self.proxys[self.i]+Fore.WHITE)

            #adding use proxy to chrome options
            self.options.add_argument('--proxy-server=%s' % PROXY)#adds use proxy argument to options
            
            
            #defining our driver with proxys
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options)

    def defInStockKeywords(self,selfInStockKeywords):
        self.inStockKeywords = selfInStockKeywords

    def defOutStockKeywords(self,outStockKeywords):
        self.outStockKeywords = outStockKeywords

    def audioCue(self,audioCueBool,audioPath):
        #debug
        if (self.debugBool == True):
                print(Fore.YELLOW+"Audio enabled"+Fore.WHITE)
        self.audioCueBool = audioCueBool
        self.audioPath = audioPath
        if (self.audioCueBool == True):
            if (self.audioPath == 'default'):
                #sets path for default file
                self.audioPath = os.path.abspath('alarm.mp3')
                #this line fixes a big in the library where spaces in the path make the lib not work
            self.audioPath = self.audioPath.replace(" ", "%20")

    
    def checkInStock(self,link):

        if (self.headBool != True or self.proxyBool != True):
            #defining our driver
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.options) 

        #debug
        if (self.debugBool == True):
                print(Fore.YELLOW+'Going to provided link'+Fore.WHITE)
                print(Fore.YELLOW+'If proxies are enabled AND the program stops here, it that most likeley means the proxy is dead.'+Fore.WHITE)

        try:
            #go to page
            self.driver.get(link)
        except:
            #telling user that proxy is bad
             print(Fore.RED+'PROXY FAILED, MOVING ON'+Fore.WHITE)
             return


        #debug
        if (self.debugBool == True):
                print(Fore.YELLOW+'Scraping all text from page'+Fore.WHITE)

        #get all text from body
        self.pageText = self.driver.find_element_by_tag_name('body').text.lower().split('\n')

        #defining in stock
        self.isInStock = None

        #debug
        if (self.debugBool == True):
                print(Fore.YELLOW+'Comparing keywords'+Fore.WHITE)

        #checking for "in stock" or "out of stock" text on page
        for i in self.pageText:
            for x in self.outStockKeywords:
                if x in i:
                    self.isInStock = False
            for z in self.inStockKeywords:
                if z in i:
                    self.isInStock = True

        #debug
        if (self.debugBool == True):
                print(Fore.YELLOW+"Playing Audio"+Fore.WHITE)
        #playing audio if needed
        if (self.audioCueBool == True):
            playsound(self.audioPath)

        

        #return result 
        return(self.isInStock)

    def cleanup(self):
        #close window
        self.driver.close()

        #debug
        if (self.debugBool == True):
                print(Fore.YELLOW+'Cleanup complete'+Fore.WHITE)
        