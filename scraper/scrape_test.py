from recipe_scrapers import scrape_me

# give the url as a string, it can be url from any site listed below
scrape_me = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

title = scrape_me.title()
total_time = scrape_me.total_time()
ingredients = scrape_me.ingredients()
instructions = scrape_me.instructions()

file_name = "recipes.txt"
ingredients_string = ""
instructions_string = ""
for ing in ingredients :
    ingredients_string += ing
    ingredients_string += '\n'

# for step in instructions :
#     instructions_string += step
#     instructions_string += " "

with open(file_name, 'a') as out :
    out.write(title + '\n' + ingredients_string + '\n' + instructions + '\n')
