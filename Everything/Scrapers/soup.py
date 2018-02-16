import urllib.request as url
from bs4 import BeautifulSoup, SoupStrainer

response = url.urlopen("http://allrecipes.com/recipes/276/desserts/cakes/?page=3#2")


strainer = SoupStrainer('article',{'class:', 'fixed-recipe-card'})
soup = BeautifulSoup(response,"html.parser", parse_only=strainer)

start = 'http://allrecipes.com/'

for link in soup.find_all('a'):
    if link.has_attr('href'):
        print(link['href'])
