# InStockPy

Using InStockPy, you can check weather any item is in stock by using keywords to determine if an item is in stock. InStockPy has support for proxies to bypass anti bot protection.

## Installation

######  Python 3+ required
`pip install In-Stock-Py`

## Functions & Classes
Class creation example
`a = InStockPy.main()`

##### Debug Mode
Debug mode needs to be called before any other function in order for it to work
`a.debug(<Bool>)` 

##### Headless mode
Set this to true if you dont want to see the chrome window when the script is checking an item.
`a.headless(<Bool>)`

##### Define Keywords for an in stock item
Put keyword here that mean an item is in stock.
`a.defInStockKeywords(["add to cart","in stock"])`

#### Define Keywords for an out of stock item
Put keyword here that mean an item is out of stock.
`a.defInStockKeywords(["unavaliable","out of stock"])`

#### Sound notifiations when an item is in stock
Set path to 'default' if you want to use the default sound.
`a.audioCue(<Bool>,'C:\path\to\mp3')`

#### Use proxies
`a.useProxy(<Bool>, r"C:\path\to\prox.txt",<int [amount of times to reuse proxy]>)`

#### Check if in stock
Set link that you want to check.
Returns <Bool>, True = In Stock, False = Out of stock, None = no keywords found on page
`a.checkInStock(r'https://link-to-product.com')`

#### Final cleanup
`a.cleanup()` Closes webdriver, open threads, etc.

## Usage Wthout Loops

The program below will return weather or not an item is in stock based off of keywords defined below.

```python
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
```

## Usage With Loops
The usage below uses a while true loop to check if an item is in stock forever. It uses proxys to bypass bot protection and plays an alarm sound when it is in stock.  
```python
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
````


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Add me on discord `Zexter#0323`

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
