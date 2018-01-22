from recipe_scrapers import scrape_me
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request as url
from bs4 import BeautifulSoup, SoupStrainer

webpages = ['http://thepioneerwoman.com/cooking_cat/cakes/', 'http://thepioneerwoman.com/cooking_cat/cakes/page/2/',
            'http://thepioneerwoman.com/cooking_cat/cakes/page/3/', 'http://thepioneerwoman.com/cooking_cat/cookies/',
            'http://thepioneerwoman.com/cooking_cat/cookies/page/2/', 'http://thepioneerwoman.com/cooking_cat/cookies/page/3/',
            'http://thepioneerwoman.com/cooking_cat/pies/', 'http://thepioneerwoman.com/cooking_cat/pies/page/2/']

for page in webpages:
    response = url.urlopen(page)


    strainer = SoupStrainer('article',{'class', 'post-card-vertical category-cooking'})
    soup = BeautifulSoup(response,"html.parser", parse_only=strainer)

    soup = soup.find_all('a')
    nodupes = []
    for link in soup:
        if link.has_attr('href'):
            nodupes.append(link['href'])
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
                out.write(title + '\n' + ingredients_string + '\n' + instructions + '\n')
        except:
            print("not a recipe")

