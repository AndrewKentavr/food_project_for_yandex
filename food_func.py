from globals import Globals
import requests


def search_recipes(recipe):
    req = 'https://api.spoonacular.com/recipes/complexSearch'

    food_params = {'apiKey': Globals.apiKey_spoonacular_1,
                   'query': recipe}

    response = requests.get(req, params=food_params)

    try:
        assert response
        json_response = response.json()
        try:
            id_recipe = json_response['results'][0]['id']
            image_recipe = json_response['results'][0]['image']
            print(id_recipe, image_recipe)
            return [id_recipe, image_recipe]
        except IndexError:
            return "IndexError"
    except AssertionError:
        return "AssertionError"
