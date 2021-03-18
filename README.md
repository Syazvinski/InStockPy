# In-Stock Bot

This bot allows you to check if any item is in stock on any website with proxy funcionality.

## Installation

Just download this project as a zip and extract it. Then open the example file and give it a run.

## Prerequisites
python 3+

`pip install selenium` for web parsing

`pip install colorama` for colored console

`pip install pyttsx3` for tts

`pip install playsound` for alert sound

`pip install chromedriver-py` for selenium

`pip install webdriver_manager` also for selenium


## Usage

```python
import mainScript

#url to check for stock
url = 'https://www.target.com/p/playstation-5-console/-/A-81114595'

#website name(for tts and console alerts)
platform = '(Target)'

#price of product (for tts and console alerts)
price = '499$'

#name of product (for tts and console alerts)
name = 'PlayStation 5 Console'

#keywords to check page for to determine if item is in stock  KEEP LOWERCASE
inStockKeywords = ["delivery","pick up","in stock","add to cart"]

#keywords to check page for to determine if item is out of stock  KEEP LOWERCASE
outStockKeywords = ["sold out","out of stock","coming soon"]

#Set this to True if you would like to use proxies. Proxies can be edited in the proxys.txt file.
useProxys = True

#function to call to loop check if in stock
mainScript.mainLoop(url,platform,price,name,inStockKeywords,outStockKeywords,useProxys)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Add me on discord `Zexter#0323`

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
