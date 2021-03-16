import mainScript

url = 'https://www.target.com/p/playstation-5-console/-/A-81114595'

platform = '(Target)'

price = '499$'

name = 'PlayStation 5 Console'

inStockKeywords = ["delivery","pick up","in stock","add to cart"]

outStockKeywords = ["sold out","out of stock","coming soon"]

mainScript.mainLoop(url,platform,price,name,inStockKeywords,outStockKeywords)

