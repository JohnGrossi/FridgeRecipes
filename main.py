import requests
import json

apiKey = "65a516019eb145fba3d0f251910c1ebc"

myRequest = requests.get("https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=2&apiKey=65a516019eb145fba3d0f251910c1ebc")

print("no errors")