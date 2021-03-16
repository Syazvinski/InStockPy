import mainScript
import time
from colorama import init, Fore, Back, Style
from datetime import datetime


init(convert=True)

def logInStock(name):
    f = open('log.txt', "a")
    f.write(name+datetime.now())
    f.close()

while True:
    print(Fore.WHITE +"Checking...")
    isSoldOut = mainScript.getStat('https://www.target.com/p/xbox-series-x-console/-/A-80790841')
    if isSoldOut == False:
        print(Fore.GREEN +"In Stock")
        logInStock("Xbox Series X Console 499$")
    else:
        print(Fore.RED +"Out Of Stock")

    time.sleep(1.5)

