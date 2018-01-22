from recipe_scrapers import scrape_me
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import urllib.request as url
from bs4 import BeautifulSoup, SoupStrainer

# driver = webdriver.Chrome()
# driver.get("http://allrecipes.com/recipes/276/desserts/cakes/?page=3#2")
# assert "Cake" in driver.title
#
# wait = WebDriverWait(driver, 10)

response = url.urlopen("http://allrecipes.com/recipes/276/desserts/cakes/?page=18#18")


strainer = SoupStrainer('article', {'class:', 'fixed-recipe-card'})
soup = BeautifulSoup(response,"html.parser", parse_only=strainer)

start = 'http://allrecipes.com'

file_name = "allrecipes_recipes.txt"


for link in list(set(soup.find_all('a'))):
    if link.has_attr('href'):
        print(link['href'][1:7])
        if link['href'][1:7] == "recipe" :
            link = start + link['href']
            print(link)
            scrape_mes = scrape_me(link)
            title = scrape_mes.title()
            ingredients = scrape_mes.ingredients()
            instructions = scrape_mes.instructions()

            ingredients_string = ""
            instructions_string = ""
            for ing in ingredients :
                ingredients_string += ing
                ingredients_string += '\n'
            with open(file_name, 'a') as out :
                out.write(title + '\n' + ingredients_string + '\n' + instructions + '\n')
