import requests
import random

base_url = 'https://api.ng.termii.com/api'


class Templates:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_template(self, phone_number, device_id, template_id, product_name, expiry_time, otp=None):
        url = base_url + f'/send/template'
        if otp is not None:
            otp_val = otp
        else:
            otp_val = random.randint(99999, 999999)
        payload = {
            "phone_number": phone_number,
            "device_id": device_id,
            "template_id": template_id,
            "api_key": self.api_key,
            "data": {
                "product_name": product_name,
                "otp": otp_val,
                "expiry_time": expiry_time
            }
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
