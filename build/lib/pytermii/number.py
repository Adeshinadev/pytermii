import requests

base_url = 'https://api.ng.termii.com/api'


class NumberMessage:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_message(self, to, sms):
        url = base_url + f'/sms/number/send'
        payload = {
            "to": to,
            "sms": sms,
            "api_key": self.api_key
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

