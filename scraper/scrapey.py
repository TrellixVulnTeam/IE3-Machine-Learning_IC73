from recipe_scrapers import scrape_me
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("http://allrecipes.com/recipes/276/desserts/cakes/?page=3#2")
assert "Cake" in driver.title
elems = driver.find_elements_by_class_name("fixed-recipe-card")
ii = 0

file_name = "recipes.txt"

while ii <=2:
    for recipe in elems:
        a_tag = recipe.find_element_by_tag_name("a")
        link = a_tag.get_attribute("href")
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
        ii += 1
