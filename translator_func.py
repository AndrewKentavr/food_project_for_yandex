from globals import Globals
import requests


def english_trans(text):
    req = 'https://translate.api.cloud.yandex.net/translate/v2/translate'

    params = {'folder_id': Globals.id_yandex,
              "texts": text,
              "targetLanguageCode": "en"}

    hed = {
        'Authorization': Globals.apiKey_yandex_translator
    }

    response = requests.post(req, params=params, headers=hed)
    try:
        assert response
        json_response = response.json()
        try:
            return json_response['translations'][0]['text']
        except IndexError:
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"


def detect_language(text):
    req = 'https://translate.api.cloud.yandex.net/translate/v2/detect'

    params = {"text": text,
              'folder_id': Globals.id_yandex,
              }

    hed = {
        'Authorization': Globals.apiKey_yandex_translator
    }

    response = requests.post(req, params=params, headers=hed)
    try:
        assert response
        json_response = response.json()
        try:
            return json_response['languageCode']
        except IndexError:
            print("IndexError")
            return "IndexError"
    except AssertionError:
        print("AssertionError")
        return "AssertionError"
