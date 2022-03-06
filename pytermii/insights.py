import json

import requests

base_url = 'https://api.ng.termii.com/api'


class Insight:
    def __init__(self, api_key):
        self.api_key = api_key

    def balance(self):
        url = base_url + f'/get-balance?api_key={self.api_key}'
        response = requests.get(url)
        return response.json()

    def search(self, phone_number):
        url = base_url + f'/check/dnd?api_key={self.api_key}&phone_number={phone_number}'
        response = requests.get(url)
        return response.json()

    def status(self, phone_number, country_code):
        url = base_url + f'/insight/number/query?phone_number={phone_number}&api_key={self.api_key}&country_code={country_code}'
        response = requests.get(url)
        return response.json()

    def history(self):
        url = base_url + f'/sms/inbox?api_key={self.api_key}'
        response = requests.get(url)
        print(response.json())
        return response.json()
