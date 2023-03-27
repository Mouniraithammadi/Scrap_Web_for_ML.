Introduction
This is a Python script that uses Selenium and BeautifulSoup libraries to scrape product information from https://www.ingredientsonline.com. The script can be used to extract information about different types of ingredients, such as cholesterol, fat, sodium, carbohydrates, and protein. The script visits each product page, extracts the name, link, and price of the product and saves it into a dictionary.

Requirements
Python 3.x
Selenium
BeautifulSoup
Google Chrome (or any other browser supported by Selenium)
Installation
Clone the repository
Install the required libraries by running pip install -r requirements.txt in your terminal
Download and install the ChromeDriver executable from http://chromedriver.chromium.org/downloads
Replace the path/to/chromedriver in line 8 of the script with the path to your downloaded ChromeDriver executable
Usage
Open scraper.py in your preferred code editor
Replace the empty username and password variables in the script with your credentials to log in to the website
Find the XPATH for the product price element of each ingredient type by inspecting the page and copying the XPATH of the element. Replace the empty price_Xpath variable in the script with the XPATH of the product price element for each ingredient type.
Run the script by typing python scraper.py in your terminal.
Output
The script saves the information about each product into separate dictionaries for each ingredient type. Each dictionary has a key for each product named product_# where # is the index of the product. Each key contains a nested dictionary with the keys name, link, and pric, which contain the name, link, and price of the product, respectively.

Limitations
The script only scrapes the first two pages of each ingredient type. This can be changed by modifying the range function in the for loop of each ingredient type.
The script assumes that each product page contains a price element with the same XPATH. If this is not the case, the script will throw an error.
The script may not work if the website layout changes.
