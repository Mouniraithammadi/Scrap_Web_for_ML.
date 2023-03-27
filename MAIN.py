from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import requests
import json
from bs4 import BeautifulSoup
drv = webdriver.Chrome()
drv.get("https://www.ingredientsonline.com/customer/account/login/")
username = ""# put the username
password = ""# put the username
price_Xpath = '' # go to the page ,and select incspect of the price you wante , copy> XPATH , and put it in this is  variable


drv.implicitly_wait(20)
drv.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
drv.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)
drv.find_element(By.XPATH, '//*[@id="send2"]').click()




cholesterol = {}
fat = {}
sodium = {}
carbohydrate = {}
protein = { }
calcium = {}
iron = {}
potassium = {}
all_products = {}
cont = 0
number_of_product = 0




# worke now with cholesterol
for page in range(1,3):

    cholesterol_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=cholesterol"
    r = requests.get(cholesterol_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric= drv.find_element(By.XPATH,price_Xpath)
        product_save = { "name" : product.text , "link" : product.attrs['href'] , "pric": pric}
        cholesterol["product_" + str(cont)] = product_save

print("$$$____the mumber of products cholesterol is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["cholesterol"] = cholesterol
number_of_product = number_of_product + cont
cont= 0








# worke now with fat

for page in range(1,3):

    fat_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=fat"
    r = requests.get(fat_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        fat["product_" + str(cont)] = product_save

print("$$$____the mumber of products fat is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["fat"] = fat
number_of_product = number_of_product + cont
cont=0








# worke now with sodium

for page in range(1,5):

    sodium_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=sodium"
    r = requests.get(sodium_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        sodium["product_" + str(cont)] = product_save

print("$$$____the mumber of products sodium is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["sodium"] = sodium
number_of_product = number_of_product + cont
cont=0




# worke now with carbohydrate

for page in range(1,2):

    carbohydrate_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=carbohydrate"
    r = requests.get(carbohydrate_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        carbohydrate["product_" + str(cont)] = product_save

print("$$$____the mumber of products carbohydrate is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["carbohydrate"] = carbohydrate
number_of_product = number_of_product + cont
cont=0






# worke now with protein

for page in range(1,6):

    protein_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=protein"
    r = requests.get(protein_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        protein["product_" + str(cont)] = product_save

print("$$$____the mumber of products protein is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["protein"] = protein
number_of_product = number_of_product + cont
cont=0





# worke now with calcium

for page in range(1,6):

    calcium_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=calcium"
    r = requests.get(calcium_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        calcium["product_" + str(cont)] = product_save

print("$$$____the mumber of products calcium is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["calcium"] = calcium
number_of_product = number_of_product + cont
cont=0







# worke now with iron

for page in range(1,2):

    calcium_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=iron"
    r = requests.get(calcium_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        iron["product_" + str(cont)] = product_save

print("$$$____the mumber of products iron is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["iron"] = iron
number_of_product = number_of_product + cont
cont=0












# worke now with potassium

for page in range(1,3):

    calcium_url = "https://www.ingredientsonline.com/catalogsearch/result/index/?p="+ str(page)+"&product_list_limit=40&q=potassium"
    r = requests.get(calcium_url)
    source = r.content
    allData = BeautifulSoup(source, "html.parser")
    zone = allData.find("ol", {"class": "products list items product-items"})
    products = zone.find_all("a",{"class":"product-item-link"})
    for product in products:
        cont = cont + 1
        drv.get(product.attrs['href'])
        pric = drv.find_element(By.XPATH,price_Xpath)
        product_save = {"name": product.text,"link": product.attrs['href'],"pric": pric}
        potassium["product_" + str(cont)] = product_save

print("$$$____the mumber of products potassium is "+ str(cont - 1) + " and it save it successfully____$$$ ")
all_products["potassium"] = potassium
number_of_product = number_of_product + cont
print("all the products is " + str(number_of_product))

















with open("products.json" , "w" , encoding="utf-8") as file :
    json.dump( all_products, file , ensure_ascii= False , indent= 4)








