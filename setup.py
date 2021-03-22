from distutils.core import setup

# read the contents of your README file
from os import path
from io import open
#try:
  #this_directory = path.abspath(path.dirname(__file__))
  #with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
      #long_description = f.read()
#except:
  #long_description = "Failure"

setup(
  name = 'InStockPy',         # How you named your package folder (MyLib)
  packages = ['InStockPy'],   # Chose the same as "name"
  version = '0.2.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Checks if an item is in stock at any link based off of specified keywords using selenium and proxys.',   # Give a short description about your library
  #long_description=long_description,
  #long_description_content_type='text/markdown',
  author = 'Stephan Yazvinski',                                                                                                                           # Type in your name
  author_email = 'syazivnski@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Syazvinski/InStockPy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Syazvinski/InStockPy/archive/refs/tags/0.2.3tar.gz',    # I explain this later on
  keywords = ['In', 'Stock', 'Checker','Proxy','Selenium','In Stock','nvidia','bot','scalper'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'selenium',
          'colorama',
          'playsound',
          'chromedriver-py',
          'webdriver_manager',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: End Users/Desktop',      # Define that your audience are end users
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)