import linkGrabber

links = linkGrabber.Links('http://allrecipes.com/recipes/276/desserts/cakes/?page=3#2')
gb = links.find(limit = 10, duplicates = False, pretty = True, {'class' : 'pinterest'})
print(gb)