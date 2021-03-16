#colored console output
from colorama import init, Fore, Back, Style
init(convert=True)

#for delays
import time

#gets drops from log file and filters only last x amount of drops to display
def getDrops(amount):
    Drops = []
    drops = []

    #open and store log file
    with open('log.txt') as f:
        for line in f:
            Drops.append(line)

    #reverse log list
    Drops.reverse()

    #define x
    x = 0

    #get last z amount of drops(amount stored in "amount" var)
    for i in Drops:
        x += x
        if x < amount:
            drops.append(i)
        
    #return results
    return drops


#defining old drops
oldDrops = []

#foreverloop to check and update drop history every xin this case (5) seconds
while True:

    #getting drops and storing drops
    drops = getDrops(6)
    
    #if the drops HAVE changed 
    if drops != oldDrops:

        #print new drops
        for i in drops:
            drop = i.split(',')
            print(Fore.BLUE+drop[0]+" "+Fore.GREEN+drop[1]+" "+Fore.WHITE+drop[2]+drop[3])

        #defining after prining because this is necesary for first time run
        oldDrops = drops
    else:
        #sets old drops to new drops
        oldDrops = drops

    #wait 5 seconds
    time.sleep(5)
    