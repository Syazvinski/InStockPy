import InStockPy

#ceating class instance
a = InStockPy.main()

#debug mode true
a.debug(True)

#headless mode true
a.headless(True)

#def in stock keywords
a.defInStockKeywords(["delivery","in stock","add to cart"])

#def out of stock keywords
a.defOutStockKeywords(["sold out","out of stock","coming soon"])

#play audio when in stock
a.audioCue(True,'default')

while True:
    #use proxies true
    a.useProxy(True, r"C:\Users\proxies.txt",1)

    #check if in stock and print result
    print(a.checkInStock(r'https://link-to-product.com')))