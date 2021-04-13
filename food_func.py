from globals import Globals
import requests


class Recipes():
    def search_recipes(self, query):
        req = 'https://api.spoonacular.com/recipes/complexSearch'

        food_params = {'apiKey': Globals.apiKey_spoonacular_1,
                       'query': query}

        response = requests.get(req, params=food_params)

        try:
            assert response
            json_response = response.json()
            try:
                id_recipe = json_response['results'][0]['id']
                image_recipe = json_response['results'][0]['image']
                return [id_recipe, image_recipe]
            except IndexError:
                return "IndexError"
        except AssertionError:
            return "AssertionError"

    def recipe_information(self, id):
        req = f'https://api.spoonacular.com/recipes/{id}/information'
        food_params = {'apiKey': Globals.apiKey_spoonacular_1}

        response = requests.get(req, params=food_params)

        try:
            assert response
            json_response = response.json()
            try:
                summary = json_response['summary']

                cc = summary.split('<b>')

                num = [i for i in range(len(cc)) if 'calories' in cc[i]][0]

                cal = cc[num].split('</b>')[0]
                prot = cc[num].split('</b>')[0]
                fat = cc[num].split('</b>')[0]

                return [cal, prot, fat]
            except IndexError:
                return "IndexError"
        except AssertionError:
            return "AssertionError"

    def random_recipes(self):
        req = 'https://api.spoonacular.com/recipes/random'
        food_params = {'apiKey': Globals.apiKey_spoonacular_1}

        response = requests.get(req, params=food_params)

        try:
            assert response
            json_response = response.json()
            try:
                return json_response['recipes']
            except IndexError:
                return "IndexError"
        except AssertionError:
            return "AssertionError"

    def recipe_ingredients_id(self, id):
        req = f'https://api.spoonacular.com/recipes/{id}/ingredientWidget.json'
        food_params = {'apiKey': Globals.apiKey_spoonacular_1}

        response = requests.get(req, params=food_params)

        try:
            assert response
            json_response = response.json()
            try:
                return json_response['ingredients']
            except IndexError:
                return "IndexError"
        except AssertionError:
            return "AssertionError"


class Ingredient:
    def ingredient_search(self, query):
        req = 'https://api.spoonacular.com/food/ingredients/search'

        food_params = {'apiKey': Globals.apiKey_spoonacular_1,
                       'query': query}

        response = requests.get(req, params=food_params)

        try:
            assert response
            json_response = response.json()
            try:
                id_ingred = json_response['results'][0]['id']
                image_ingred = json_response['results'][0]['name']
                return [id_ingred, image_ingred]
            except IndexError:
                return "IndexError"
        except AssertionError:
            return "AssertionError"
    def ingredient_information(self, id):
        req = f'https://api.spoonacular.com/food/ingredients/{id}/information'
        food_params = {'apiKey': Globals.apiKey_spoonacular_1}

        response = requests.get(req, params=food_params)

        try:
            assert response
            json_response = response.json()
            try:
                pass
            except IndexError:
                return "IndexError"
        except AssertionError:
            return "AssertionError"