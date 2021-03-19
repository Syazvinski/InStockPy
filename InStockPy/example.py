import InStockPy

#ceating class instance
a = InStockPy.main()

#headless mode true
a.headless(True)

#def in stock keywords
a.defInStockKeywords(["delivery","in stock","add to cart"])

#def out of stock keywords
a.defOutStockKeywords(["sold out","out of stock","coming soon"])

#check if in stock and print result
print(a.checkInStock(r'https://link-to-product.com')))

#preforming final cleanup
a.cleanup() 