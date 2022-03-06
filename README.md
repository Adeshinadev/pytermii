# Pytermii

[![image](https://img.shields.io/travis/ZEDGR/pychal.svg)](https://travis-ci.org/ZEDGR/pychal)

Pytermii provides python bindings for the [TERMII API](https://developers.termii.com/).
The pytermii module was created by [Aina Adeshina](https://github.com/adeshinadev)


# Requirements

- `requests`
- `json`

# Python version support

- `2.7`
- `3.4+`

# Installation

For the stable version

    pip install pytermii

# Usage

```python
from pytermii.termii import Termii

# Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
termii = Termii('your_api_key')

# Retrieve the status of all registered sender ID.
sender_ids=termii.sender_id.fetch()

# Tournaments, matches, and participants are all represented as normal Python dicts.
print(print(termii.sender_id.fetch()['data'][0]['sender_id'])) # ACME Key
print(termii.sender_id.fetch()['data'][0]['status']) # unblock

# Request registration of sender ID and print the request code 
termii.sender_id.request_id('Acme', 'Your OTP code is zxsds', 'Acme Corp')

# send text message to a number
# the parameter are to, from_id, sms, type, channel)
# you can see the possible value for the parameter at https://developers.termii.com/messaging
termii.message.send_message('2349133370715', 'ACME', 'A message from pytermii', 'plain', 'generic')

# send bulk message
# the parameter are to (a list of recipient phone number), from_id, sms, type, channel
# you can see the possible value for the parameter at https://developers.termii.com/messaging
termii.message.send_bulk_message(['2349133370715'], 'ACME', 'A message from pytermii', 'plain', 'generic')

# send messages to customers using Termii's auto-generated messaging numbers that adapt to customers location.
# the parameter are to (recipient phone number) and sms
# you can see the possible value for the parameter at https://developers.termii.com/number
termii.number.send_message('2349133370715', "Hi there, testing pytermii")

# set a template for the one-time-passwords (pins) sent to their customers via whatsapp or sms.
# the parameter are phone_number, device_id, template_id, product_name, expiry_time, otp
# otp is automatically generated if none is provided
# you can see the possible value for the parameter at https://developers.termii.com/templates
termii.template.send_template('2349133370715', 'talert', '1493-csdn3-ns34w-sd3434-dfdf', 'Termii', '120435','10 minutes')

# view all phonebooks
termii.phonebook.fetch()

# Create a Phonebook
# you can see the possible value for the parameter at https://developers.termii.com/phonebook
termii.phonebook.create("Phone test", "Phonebook for test")

# Update a Phonebook by name
termii.phonebook.update_by_name('old phonebook name', 'new phonebook name', "Phonebook for test")

# Create a Phonebook
# in case of positional argument,the parameters are phonebook_id, new_phonebook_name new_description
termii.phonebook.update_by_id('phonebook_id', 'new_phonebook_name', 'new_phonebook_description')

# delete a Phonebook
termii.phonebook.delete_by_name('phonebook_id')


# Send a campaign by name
termii.campaign.send_campaign_by_name('phonebook_name', '234', 'sender_id', 'Welcome to Termii.', 'generic', 'Plain', 'personalized', 'scheduled', '30-06-2022 6:00')

# Send a campaign by ID
termii.campaign.send_campaign_by_id('phonebook_id', '234', 'sender_id', 'Welcome to Termii.', 'generic', 'Plain', 'personalized', 'scheduled', '30-06-2022 6:00')

# Fetch campaigns
termii.campaign.fetch_campaigns()

# Fetch campaign history
termii.campaign.fetch_campaign_history('campaign_id')

# Send token
# you can see the possible value for the parameter at https://developers.termii.com/send-token
termii.token.send_token('message_type', '2349133370715', 'Aproved Sender or Device IDs', 'channel', 'pin_attempts', 'pin_time_to_live', 'pin_length', "pin_placeholder", "message_text","pin_type")

# Voice Token
# you can see the possible value for the parameter at https://developers.termii.com/voice-token
termii.token.voice_token('phone_number', 'pin_attempts', 'pin_time_to_live', 'pin_length')

# Voice Call
# you can see the possible value for the parameter at https://developers.termii.com/voice-call
termii.token.voice_call('phone_number', 'code')

# In-App Token
# you can see the possible value for the parameter at https://developers.termii.com/in-app-token
termii.token.in_app_token('pin_type', 'phone_number', 'pin_attempts', 'pin_time_to_live', 'pin_length')

# Verify Token
# you can see the possible value for the parameter at https://developers.termii.com/in-app-token
termii.token.verify_token('pin_id', 'pin')


# Total balance and balance information from your wallet
# you can see the possible value for the parameter at https://developers.termii.com/balance
termii.insight.balance()

# Verify phone numbers and automatically detect their status as well as current network.
# you can see the possible value for the parameter at https://developers.termii.com/search
termii.insight.search('phone_number')

# detect if a number is fake or has ported to a new network.
# you can see the possible value for the parameter at https://developers.termii.com/status
termii.insight.status('phone_number', 'country_code')

#  reports for messages sent across the sms, voice & whatsapp channels.
# you can see the possible value for the parameter at https://developers.termii.com/history
termii.insight.history()
```

See [termii.com](https://developers.termii.com/) for full API
documentation.

