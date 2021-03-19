from distutils.core import setup

import io
with io.open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'InStockPy',         # How you named your package folder (MyLib)
  packages = ['InStockPy'],   # Chose the same as "name"
  version = '0.1.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Checks if an item is in stock based off of keywords.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Stephan Yazvinski',                   # Type in your name
  author_email = 'syazivnski@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Syazvinski/InStockPy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Syazvinski/In-Stock-Py/archive/refs/tags/0.1.5.tar.gz',    # I explain this later on
  keywords = ['In', 'Stock', 'Checker','Proxy','Selenium','In Stock'],   # Keywords that define your package best
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