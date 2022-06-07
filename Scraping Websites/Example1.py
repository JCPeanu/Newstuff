import requests #to interact with the internet
from bs4 import BeautifulSoup #this package can understand HTML code
 
#first tell requests to get the webpage info
URL = "https://www.marketwatch.com/investing/stock/goog"
web = requests.get(URL)
 
#some info of the webpage
#print(web.headers['content-type'])
#print(web.text)
 
# #now tell Beautiful Soup to read it (parse it) becuase it knows how to interpret it
# soup = BeautifulSoup(web.content, 'html.parser')
 
# #uncomment some of the next lines to see what they do. read the documentation to get further info.
# #print(soup.prettify())
# #print(soup.title)
# #print(soup.title.name)
# #print(soup.title.string)
# #print(soup.meta)
 
# #find() will look for the first occurence
# #print(soup.find("meta"))
 
# #findAll() will find all occurences and put them into a list
# #print(soup.findAll('meta'))
 
# #find all parts that have the metadata but select only those that have as an internal value name="description"
# #print(soup.findAll('meta', {'name': 'description'}))
 
# #find all sections that mention a table at the start
# #print(soup.findAll("table"))
 
# #from the previous set, select only those that have the config class="ratesTable"
# #print(soup.findAll("table", {"class": "ratesTable"}))
 
# #from the previous list, select only the first element (the first table)
# #print(soup.findAll("table", {"class": "ratesTable"})[0])
 
# #from that table, find all the part that mention a "tbody"
# #print(soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody"))
 
# #now save it into a variable
# ratelist = soup.findAll("table", {"class": "ratesTable"})[0].findAll("tbody")
 
# #Now iterate over that list
# for table_value in ratelist:
#     #and find only the parts that mention a "tr" value (inspect the webpage)
#     trade_list = table_value.findAll('tr')
#     #now iterate again over that list that contains the values for the different currencies (only three iterations, you can change the number)
#     for trade_value in trade_list[:3]:
#         #and print ONLY the text part
#         print(trade_value.text)
 
soup = BeautifulSoup(web.content, "html.parser")
print(soup.findAll('h1'))
print(soup.findAll('h2'))
print(soup.find('h2', {'class': "company_name"}).text)