#print("hello world")

import requests
import pandas as pd
from bs4 import BeautifulSoup
#url = "https://courses.wscubetech.com/"
#r = requests.get(url)
#print(r.status_code)
#print(r.text) #Unstructured data
#print(r)

#soup = BeautifulSoup(r.text, "lxml")
#print(soup) #Gives data in string format and will be extracted using different functions of BeautifulSoup

#Tags
#print(soup.div) #Extracting data with div tag, when theme of inspect is white then  all purple color text are tags e.g. div, header, etc.
#tag = soup.div

#Attributes
#when theme of inspect is white then  all yellow or orangish color text are attributes e.g. class, id, etc.
#print(tag.attrs)#See attributes of tag in the form of dictionary, keys represents attributes and values represents values of attributes
#have multiple attributes, can get the value of prticular attribute
#atb = tag.attrs
#print(atb["class"])
#print(atb["style"])'''

#Navigable strings
#when theme of inspect is white then  all black color text are Navigable strings.
#url ="https://webscraper.io/test-sites/e-commerce/allinone/"
#r = requests.get(url)
#soup = BeautifulSoup(r.text, "lxml")
#tag = soup.div.p #get output with p tags as, <p>Web Scraper</p>
#tag = soup.div.p.string #get output without p tags as, Web Scraper
#Also
#tag = soup.div.p
#print(tag.string) #get output without p tags as, Web Scraper
#if navigable string inside multiple tags, go inside the tags, inside the tags.....
#tag = soup.header.div.div.a.button.span
#print(tag.string)

#find(), find() works with only first tag...
'''
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
'''
#print(soup.find('div'))
#print(soup.find("h4", {"class":"float-end price card-title pull-right"}))
'''
a = soup.find("h4", {"class":"float-end price card-title pull-right"})
print(a.string)
desc = soup.find("p", {"class":"description card-text"})
print(desc.string)
#other way of writing class
desc_ = soup.find("p", class_ = "description card-text")
print(desc_.string)
'''

#find_all()
'''
prices = soup.find_all("h4", class_ = "float-end price card-title pull-right")
print(prices)
print(len(prices))
for i in prices:
    print(i.string)
print(prices[3])
print(prices[3].text)
print(prices[3].string)
desc = soup.find_all("p", class_ = "description card-text")
print(desc[3])
print(desc[3].string)
'''

#find_all with Regex
'''
import re #stands for regular expression, helps find pattern in a string and then it extracts the data related to that pattern
#data = soup.find_all(["h4","a","p"]) #extracting data from multiple tags
#data = soup.find_all(string = "Galaxy Tab") #extracting exact data
data = soup.find_all(string = re.compile("Galaxy")) #extracting all data related to Galaxy on page
print(data)
print(len(data)) #how many times Galaxy appears
'''

#find_all with Pandas
'''
names = soup.find_all("a", class_ = "title")
product_names = []
for i in names:
    name = i.text
    product_names.append(name)
print(product_names)
prices = soup.find_all("h4", class_ = "float-end price card-title pull-right")
product_prices = []
for i in prices:
    price = i.text
    product_prices.append(price)
print(product_prices)
descs = soup.find_all("p", class_ = "description card-text")
product_desc = []
for i in descs:
    desc = i.text
    product_desc.append(desc)
print(product_desc)
reviews = soup.find_all("p", class_ = "float-end review-count")
product_reviews = []
for i in reviews:
    review = i.text
    product_reviews.append(review)
print(product_reviews)
import pandas as pd
df = pd.DataFrame({"Product Name":product_names, "Prices":product_prices, "Descriptions":product_desc, "Reviews":product_reviews})
print(df)
df.to_csv("products_details.csv")
'''

#Extract Data from Nested HTML Tags
#boxes = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")
#print(boxes)
#print(len(boxes))
'''
box = soup.find_all("div", class_ = "col-md-4 col-xl-4 col-lg-4")[3]
name = box.find("a").text
print(name)
desc = box.find("p", class_ = "description card-text").text
print(desc)
'''

#Scrape a Table From a Website using BeautifulSoup
'''
url = "https://ticker.finology.in/"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_ = "table table-sm table-hover screenertable")
#print(table)
headers = table.find_all("th")
#print(headers)
titles = []
for i in headers:
    title = i.text
    titles.append(title)
#print(titles)
df = pd.DataFrame(columns=titles)
#print(df)
rows = table.find_all("tr")
#print(rows)

for i in rows[1:]:
    #print(i.text)
    data = i.find_all("td")
    row = [tr.text for tr in data]
    #print(row)
    l = len(df)
    df.loc[l] = row
print(df)
Above loop gives \n in table

#Removing \n from table
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("a", class_="complink").text.strip()
    data = i.find_all("td")[1:]
    row = [first_td] + [tr.text.strip() for tr in data]
    l = len(df)
    df.loc[l] = row
print(df)
'''

#Scrape Multiple Pages on Websites
'''
url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text, "lxml")
while true:
    np = soup.find("a", class_ = "_1LKTO3").get("href")
    #print(np)
    cnp = "https://www.flipkart.com" + np
    #print(cnp)
    
    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    #This code is for pages having different links, incase we have changing only numbers at the end of page like flipcart we use below code
    '''
'''
for i in range(2, 11):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    # print(r)
    soup = BeautifulSoup(r.text, "lxml")
    np_tag = soup.find("a", class_="_1LKTO3")
    if np_tag:
        np = np_tag.get("href")
        # print(np)
        cnp = "https://www.flipkart.com" + np
        print(cnp)
        url = cnp
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")
    else:
        print(f"No product link found for page {i-1}")
'''
#Extracting data
'''
Names = []
Prices = []
Desc = []
Reviews = []
for i in range(1, 5):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    print(url)
    print(r)
    soup = BeautifulSoup(r.text, "lxml")
    #box = soup.find("div", class_="_1YokD2 _3Mn1Gg")
    names = soup.find_all("div", class_="_4rR01T")
    for j in names:
        name = j.text
        Names.append(name)
    print(len(Names))
    prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    for k in prices:
        price = k.text
        Prices.append(price)
    print(len(Prices))
    descs = soup.find_all("ul", class_="_1xgFaf")
    for l in descs:
        desc = l.text
        Desc.append(desc)
    print(len(Desc))
    reviews = soup.find_all("div", class_="_3LWZlK")
    for m in reviews:
        review = m.text
        Reviews.append(review)
    print(len(Reviews))
df = pd.DataFrame({"Product Names": Names, "Product Reviews": Reviews, "Product Prices": Prices, "Product Descriptions": Desc, "Product Reviews": Reviews})
df.to_csv("mobiles.csv")
'''

