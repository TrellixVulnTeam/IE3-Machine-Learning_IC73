from recipe_scrapers import scrape_me
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request as url
from bs4 import BeautifulSoup, SoupStrainer

base = 'https://www.epicurious.com/search/?meal=dessert&type=cake%2Ccookie%2Ccupcake%2Cbrownie%2Ccheesecake&content=recipe'
start = 'https://www.epicurious.com'

page_nums = list(range(1,122))

for page in page_nums:
    if page == 1:
        site = base
    else:
        site = base + '&page=' + str(page)
    response = url.urlopen(site)


    strainer = SoupStrainer('article',{'class', 'recipe-content-card'})
    soup = BeautifulSoup(response,"html.parser", parse_only=strainer)

    soup = soup.find_all('a')
    nodupes = []
    for link in soup:
        if link.has_attr('href'):
            link = start + link['href']
            nodupes.append(link)
    nodupes = list(set(nodupes))

    file_name = "recipes.txt"

    for link in nodupes:
        try :
            scrape_mer = scrape_me(link)
            title = scrape_mer.title()
            ingredients = scrape_mer.ingredients()
            instructions = scrape_mer.instructions()

            ingredients_string = ""
            instructions_string = ""
            for ing in ingredients :
                ingredients_string += ing
                ingredients_string += '\n'
            with open(file_name, 'a') as out :
                out.write(title + '\n' + ingredients_string + '\n' + instructions + '\n' +'\n')
        except:
            print("not a recipe")

