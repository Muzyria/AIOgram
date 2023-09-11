import requests
import json


my_token = ''
chat_id = ''
first_name = ''
text = 'Hello '

def getUpdates(token):
    global chat_id
    global first_name

    api_url = f'https://api.telegram.org/bot{token}/getUpdates'

    response = requests.get(api_url)   # Отправляем GET-запрос и сохраняем ответ в переменной response

    if response.status_code == 200:    # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
        # print(response.text)
        # print()

        data = json.loads(response.text)['result']
        # print(data)
        print()
        chat_id = data[0]['message']['chat']['id']
        first_name = data[0]['message']['chat']['first_name']

    else:
        print(response.status_code)    # При другом коде ответа выводим этот код


def sendMessage(token, chat_id, text, first_name):
    api_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}, {first_name}!'
    response = requests.get(api_url)  # Отправляем GET-запрос и сохраняем ответ в переменной response
    print(json.loads(response.text))


def cats():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    print(response.text)

# getUpdates(my_token)
# print(chat_id)
# print(first_name)
# print()

# sendMessage(my_token, chat_id, text, first_name)


cats()
