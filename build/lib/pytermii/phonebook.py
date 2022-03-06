import json

import requests

base_url = 'https://api.ng.termii.com/api'


class Phonebook:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch(self):
        url = base_url + f'/phonebooks?api_key={self.api_key}'
        response = requests.get(url)
        return response.json()

    def create(self, name, desc=None):
        url = base_url + f'/phonebooks'
        payload = {
            "api_key": self.api_key,
            "phonebook_name": name,
            "description": desc
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)

        return response.json()

    def update_by_name(self, old_phonebook_name, new_phonebook_name=None, new_description=None):

        phonebooks = Phonebook(self.api_key)
        all_phonebooks = phonebooks.fetch()
        phonebook_id = 'id'
        if new_phonebook_name or new_description:
            for i in all_phonebooks['data']:
                if i['name'] == old_phonebook_name:
                    phonebook_id = i['id']
                else:
                    pass
            url = base_url + f'/phonebooks/{phonebook_id}'
            payload = {
                "api_key": self.api_key,
                "phonebook_name": new_phonebook_name,
                "description": new_description,
            }
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.patch(url, headers=headers, json=payload)
            return response.json()
        else:
            message = {'message': 'please provide a value to update,either new_phonebook_name or new_description'}
            return json.dumps(message)

    def update_by_id(self, phonebook_id, new_phonebook_name=None, new_description=None):

        url = base_url + f'/phonebooks/{phonebook_id}'
        payload = {
            "api_key": self.api_key,
            "phonebook_name": new_phonebook_name,
            "description": new_description,
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.patch(url, headers=headers, json=payload)

        return response.json()

    def delete_by_name(self, phonebook_name):

        phonebooks = Phonebook(self.api_key)
        all_phonebooks = phonebooks.fetch()
        phonebook_id = 'id'
        if phonebook_name:
            for i in all_phonebooks['data']:
                if i['name'] == phonebook_name:
                    phonebook_id = i['id']
                else:
                    pass
            url = base_url + f'/phonebooks/{phonebook_id}?api_key={self.api_key}'
            response = requests.delete(url)
            return response.json()
        else:
            message = {'message': 'please provide a value for phonebook_name'}
            return json.dumps(message)

    def delete_by_id(self, phonebook_id):

        url = base_url + f'/phonebooks/{phonebook_id}?api_key={self.api_key}'
        response = requests.delete(url)
        return response.json()
