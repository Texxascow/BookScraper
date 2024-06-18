#dependencies
from bs4 import BeautifulSoup
import requests 
import os 
from dotenv import load_dotenv
from pprint import pprint

#Book Website URL 
URL = f'https://books.toscrape.com/catalogue/category/books_1/index.html'

#Bring HTML Text
CHECKVAR = requests.get(URL)

#If there is a status response, run program
if CHECKVAR.status_code == 200:


#Sidebar Content Pull 
    CONTENT = BeautifulSoup(CHECKVAR.text,"html.parser")

#find content from the sidebar and list it out 
    SIDEBAR = CONTENT.find('aside', class_= 'sidebar col-sm-4 col-md-3')
    SIDEBAR2 = SIDEBAR.find('li').get_text(strip=True, separator=', ')

#Print all available book genres 
    print(f'\nListed Categories on BooktoScrape website: \n')
    print(f'{SIDEBAR2}\n')


#Pull a random assortment of books from the front page
    BOOKTITLES = CONTENT.find('ol', class_='row')
    BOOKTITLES2 = BOOKTITLES.find_all('li')

#Front page book statistics 
    print(f'\n\nFront Page Books: \n')

    for li in BOOKTITLES2:
        print(li.get_text(strip=True, separator=' // '))

    print('\n')

#If website doesn't respond then then print this statement 
else:
    print('something went wrong')



    












