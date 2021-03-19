import mainObjOriented

#ceating class instance
a = mainObjOriented.main()

#gives you console confirmation of what going on behind the scenes (normally it prints in yellow text)
a.debug(True)

#enables headless mode
a.headless(True)

#keywords to check page for to determine if item is in stock  KEEP LOWERCASE
a.defInStockKeywords(["delivery","pick up","in stock","add to cart"])

#keywords to check page for to determine if item is out of stock  KEEP LOWERCASE
a.defOutStockKeywords(["sold out","out of stock","coming soon"])

#play a sound when an ite you are tracking comes in stock ('default' will play a default alarm sound)
a.audioCue(True,'default')

while True:
    #Set this to True if you would like to use proxies. Path to .TXT with proxys must be provided
    #if you are using this in a loop you need to call this in your loop to switch to the next proxy
    #(<useProxiesBool>,<path to .txt>,<amount of times to reuse proxy>)
    a.useProxy(True, r"C:\Users\proxies.txt",1)

    #function to call to loop check if in stock that takes link to item to check
    print(a.checkInStock(r'https://www.target.com/p/playstation-5-console/-/A-81114595'))

    #preforms cleanup closing open threads etc (this is function is recomended to run at the end of each script)
    a.cleanup()