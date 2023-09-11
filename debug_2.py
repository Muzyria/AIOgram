import json
import my_
import requests
import time


API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = ''
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
TEXT: str = 'Ура! Классный апдейт!'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
chat_id: int


while counter < 100:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет



    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}')

    data = json.loads(updates.text)['result']
    print(data)

    if data:
        offset = data[0]['update_id']
        chat_id = data[0]['message']['from']['id']
        # requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

        cat_response = requests.get(API_CATS_URL)
        if cat_response.status_code == 200:
            cat_link = cat_response.json()[0]['url']
            requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
        else:
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
