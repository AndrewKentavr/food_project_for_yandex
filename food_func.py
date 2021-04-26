from globals import Globals
import requests


def search_recipes(query):
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


def recipe_information(id):
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
            prot = cc[num + 1].split('</b>')[0]
            fat = cc[num + 2].split('</b>')[0]
            return [cal, prot, fat]
        except IndexError:
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"


def random_recipes():
    req = 'https://api.spoonacular.com/recipes/random'
    food_params = {'apiKey': Globals.apiKey_spoonacular_1}

    response = requests.get(req, params=food_params)

    try:
        assert response
        json_response = response.json()
        try:
            name = json_response['recipes'][0]['title']
            image = json_response['recipes'][0]['image']
            summary = json_response['recipes'][0]['summary']

            cc = summary.split('<b>')

            num = [i for i in range(len(cc)) if 'calories' in cc[i]][0]
            cal = cc[num].split('</b>')[0]
            prot = cc[num + 1].split('</b>')[0]
            fat = cc[num + 2].split('</b>')[0]

            id = json_response['recipes'][0]['id']
            return [name, image, cal, prot, fat, id]
        except IndexError:
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"


def recipe_ingredients_id(id):
    req = f'https://api.spoonacular.com/recipes/{id}/ingredientWidget.json'
    food_params = {'apiKey': Globals.apiKey_spoonacular_1}

    response = requests.get(req, params=food_params)

    try:
        assert response
        json_response = response.json()
        try:
            root = json_response['ingredients']
            all_ing = []
            for i in range(len(root)):
                all_ing.append(root[i]['name'])
            return all_ing
        except IndexError:
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"


# ----------------------Ingredient-----------------------------

def ingredient_search(query):
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
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"


def ingredient_information(id):
    req = f'https://api.spoonacular.com/food/ingredients/{id}/information'
    food_params = {'apiKey': Globals.apiKey_spoonacular_1,
                   'amount': 1}

    response = requests.get(req, params=food_params)

    try:
        assert response
        json_response = response.json()
        try:
            nutrients = json_response['nutrition']['nutrients']

            info = {}
            for i in range(len(nutrients)):
                if "Calories" == nutrients[i]['name']:
                    info["Calories"] = nutrients[i]

                elif "Fat" == nutrients[i]['name']:
                    info["Fat"] = nutrients[i]

                elif "Sugar" == nutrients[i]['name']:
                    info["Sugar"] = nutrients[i]

                elif "Protein" == nutrients[i]['name']:
                    info["Protein"] = nutrients[i]

                else:
                    info[nutrients[i]['name']] = nutrients[i]
            return info
        except IndexError:
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"
