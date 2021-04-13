from globals import Globals
import requests

class Translator():
    def english_trans(self):
        req = 'https://translate.api.cloud.yandex.net/translate/v2/translate'

        params = {'folder_id': 'b1ghv3pdod31alo8jrrn',
                  "texts": "чипсы",
                  "targetLanguageCode": "en"}

        hed = {
            'Authorization': 'Api-Key AQVN16eXyhRvpmU7ozpshNnfrZNwmIIsDx2FI6W7'
        }

        response = requests.post(req, params=params, headers=hed)
        print(response)
        try:
            assert response
            json_response = response.json()
            print(json_response)
            try:
                return json_response['translations'][0]['text']
            except IndexError:
                print("IndexError")
        except AssertionError:
            print("AssertionError")
