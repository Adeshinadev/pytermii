import requests

base_url = 'https://api.ng.termii.com/api'


class sender_id:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch(self):
        url = base_url + f'/sender-id?api_key={self.api_key}'
        response = requests.get(url)
        return response.json()

    def request_id(self, sender_id, usecase, company):
        url = base_url + f'/sender-id/request'
        payload = {
            "api_key": self.api_key,
            "sender_id": sender_id,
            "usecase": usecase,
            "company": company
        }
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(url, headers=headers, json=payload)
        print(requests)
        return response.text
