import requests

base_url = 'https://api.ng.termii.com/api'


class Message:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_message(self, to, from_id, sms, type, channel, media_url=None, media_caption=None):
        url = base_url + f'/sms/send'
        if media_url and media_caption:
            payload = {
                "to": to,
                "from": from_id,
                "sms": sms,
                "type": type,
                "channel": channel,
                "api_key": self.api_key,
                "media": {
                    "url": media_url,
                    "caption": media_caption
                }
            }
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.post(url, headers=headers, json=payload)
            return response.json()

        else:
            payload = {
                "to": to,
                "from": from_id,
                "sms": sms,
                "type": type,
                "channel": channel,
                "api_key": self.api_key,
            }
            headers = {
                'Content-Type': 'application/json',
            }
            response = requests.post(url, headers=headers, json=payload)
            return response.json()

    def send_bulk_message(self, to, from_id, sms, type, channel,):
        url = base_url + f'/sms/send/bulk'
        payload = {
            "to": to,
            "from": from_id,
            "sms": sms,
            "type": type,
            "channel": channel,
            "api_key": self.api_key,
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        print(response.json())
