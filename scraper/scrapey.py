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

response = url.urlopen("http://allrecipes.com/recipes/276/desserts/cakes/?page=3#2")


strainer = SoupStrainer('article',{'class:', 'fixed-recipe-card'})
soup = BeautifulSoup(response,"html.parser", parse_only=strainer)

start = 'http://allrecipes.com'


ii = 0

file_name = "recipes.txt"

while ii <=2:
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            link = start + link['href']
            try :
                scrape_me = scrape_me(link)
                title = scrape_me.title()
                ingredients = scrape_me.ingredients()
                instructions = scrape_me.instructions()

                ingredients_string = ""
                instructions_string = ""
                for ing in ingredients :
                    ingredients_string += ing
                    ingredients_string += '\n'
                with open(file_name, 'a') as out :
                    out.write(title + '\n' + ingredients_string + '\n' + instructions + '\n')
            except:
                print("not a recipe")
            ii += 1
