import requests

base_url = 'https://api.ng.termii.com/api'


class Token:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_token(self, message_type, to, from_id, channel, pin_attempts, pin_time_to_live,
                   pin_length, pin_placeholder, message_text, pin_type):
        url = base_url + f'/sms/otp/send'
        payload = {
            "api_key": self.api_key,
            "message_type": message_type,
            "to": to,
            "from": from_id,
            "channel": channel,
            "pin_attempts": int(pin_attempts),
            "pin_time_to_live": pin_time_to_live,
            "pin_length": pin_length,
            "pin_placeholder": pin_placeholder,
            "message_text": message_text,
            "pin_type": pin_type
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def voice_token(self, phone_number, pin_attempts, pin_time_to_live,
                    pin_length):
        url = base_url + f'/sms/otp/send/voice'
        payload = {
            "api_key": self.api_key,
            "phone_number": phone_number,
            "pin_attempts": int(pin_attempts),
            "pin_time_to_live": int(pin_time_to_live),
            "pin_length": int(pin_length),

        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def voice_call(self, phone_number, code):
        url = base_url + f'/sms/otp/call'
        payload = {
            "api_key": self.api_key,
            "phone_number": phone_number,
            "code": int(code)

        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def in_app_token(self, pin_type, phone_number, pin_attempts, pin_time_to_live, pin_length):
        url = base_url + f'/sms/otp/generate'
        payload = {
            "api_key": self.api_key,
            "pin_type": pin_type,
            "phone_number": phone_number,
            "pin_attempts": pin_attempts,
            "pin_time_to_live": pin_time_to_live,
            "pin_length": pin_length

        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        print(response.json())
        return response.json()

    def verify_token(self, pin_id, pin):
        url = base_url + f'/sms/otp/verify'
        payload = {
            "api_key": self.api_key,
            "pin_id": pin_id,
            "pin": pin,
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.json()
