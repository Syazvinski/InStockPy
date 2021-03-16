import mainScript

url = 'https://www.target.com/p/9-key-rack-with-4-hooks-black-nickel-threshold-8482/-/A-14034275#lnk=sametab'

platform = '(Target)'

price = '499$'

name = 'PlayStation 5 Console'

inStockKeywords = ["delivery","pick up","in stock","add to cart"]

outStockKeywords = ["sold out","out of stock","coming soon"]

useProxys = True

mainScript.mainLoop(url,platform,price,name,inStockKeywords,outStockKeywords,useProxys)

