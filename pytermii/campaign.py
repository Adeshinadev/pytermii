import json

import requests

from pytermii.phonebook import Phonebook

base_url = 'https://api.ng.termii.com/api'


class Campaign:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_campaign_by_name(self, phonebook_name, country_code, sender_id, message, channel, message_type,
                              campaign_type,
                              schedule_sms_status=None, schedule_time=None):
        phonebooks = Phonebook(self.api_key)
        all_phonebooks = phonebooks.fetch()
        phonebook_id = 'id'
        if phonebook_name:
            for i in all_phonebooks['data']:
                if i['name'] == phonebook_name:
                    phonebook_id = i['id']
                else:
                    pass
            if schedule_time and schedule_sms_status:
                payload = {
                    "api_key": self.api_key,
                    "country_code": country_code,
                    "sender_id": sender_id,
                    "message": message,
                    "channel": channel,
                    "message_type": message_type,
                    "phonebook_id": phonebook_id,
                    "delimiter": ",",
                    "remove_duplicate": "yes",
                    "campaign_type": campaign_type,
                    "schedule_time": schedule_time,
                    "schedule_sms_status": schedule_sms_status
                }
                headers = {
                    'Content-Type': 'application/json',
                }
                url = base_url + f'/sms/campaigns/send'
                response = requests.post(url, headers=headers, json=payload)

                return response.json()
            else:
                payload = {
                    "api_key": self.api_key,
                    "country_code": country_code,
                    "sender_id": sender_id,
                    "message": message,
                    "channel": channel,
                    "message_type": message_type,
                    "phonebook_id": phonebook_id,
                    "delimiter": ",",
                    "remove_duplicate": "yes",
                    "campaign_type": campaign_type,
                }
                headers = {
                    'Content-Type': 'application/json',
                }
                url = base_url + f'/sms/campaigns/send'
                response = requests.post(url, headers=headers, json=payload)
                return response.json()
        else:
            message = {'message': 'please provide a value for phonebook_name'}
            return json.dumps(message)

    def send_campaign_by_id(self, phonebook_id, country_code, sender_id, message, channel, message_type,
                            campaign_type,
                            schedule_sms_status=None, schedule_time=None):

        if schedule_time and schedule_sms_status:
            payload = {
                "api_key": self.api_key,
                "country_code": country_code,
                "sender_id": sender_id,
                "message": message,
                "channel": channel,
                "message_type": message_type,
                "phonebook_id": phonebook_id,
                "delimiter": ",",
                "remove_duplicate": "yes",
                "campaign_type": campaign_type,
                "schedule_time": schedule_time,
                "schedule_sms_status": schedule_sms_status
            }
            headers = {
                'Content-Type': 'application/json',
            }
            url = base_url + f'/sms/campaigns/send'
            response = requests.post(url, headers=headers, json=payload)
            return response.json()
        else:
            payload = {
                "api_key": self.api_key,
                "country_code": country_code,
                "sender_id": sender_id,
                "message": message,
                "channel": channel,
                "message_type": message_type,
                "phonebook_id": phonebook_id,
                "delimiter": ",",
                "remove_duplicate": "yes",
                "campaign_type": campaign_type,
            }
            headers = {
                'Content-Type': 'application/json',
            }
            url = base_url + f'/sms/campaigns/send'
            response = requests.post(url, headers=headers, json=payload)
            return response.json()

    def fetch_campaign(self):
        url = base_url + f'/sms/campaigns?api_key={self.api_key}'
        response = requests.get(url)
        print(response.json())
        return response.json()

    def fetch_campaigns(self):
        url = base_url + f'/sms/campaigns?api_key={self.api_key}'
        response = requests.get(url)
        print(response.json())
        return response.json()

    def fetch_campaign_history(self, campaign_id):
        url = base_url + f'/sms/campaigns/{campaign_id}?api_key={self.api_key}'
        response = requests.get(url)
        print(response.json())
        return response.json()



