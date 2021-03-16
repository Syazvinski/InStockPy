from colorama import init, Fore, Back, Style

import time



init(convert=True)

def getDrops():
    Drops = []
    drops = []

    with open('log.txt') as f:
        for line in f:
            Drops.append(line)

    Drops.reverse()

    x = 0

    for i in Drops:
        x += x
        if x < 10:
            drops.append(i)
        
    return drops




oldDrops = []

while True:
    drops = getDrops()
    
    if drops != oldDrops:
        for i in drops:
            drop = i.split(',')
            print(Fore.BLUE+drop[0]+" "+Fore.GREEN+drop[1]+" "+Fore.WHITE+drop[2]+drop[3])
    else:
        oldDrops = drops
    time.sleep(5)
    