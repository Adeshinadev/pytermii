from pytermii.campaign import Campaign
from pytermii.insights import Insight
from pytermii.phonebook import Phonebook
from pytermii.sender_id import sender_id
from pytermii.message import Message
from pytermii.number import NumberMessage
from pytermii.template import Templates
from pytermii.token_termii import Token

base_url = 'https://api.ng.termii.com/api'


class Termii:
    def __init__(self, api_key):
        self.api_key = api_key
        self.sender_id = sender_id(api_key)
        self.message = Message(api_key)
        self.number = NumberMessage(api_key)
        self.template = Templates(api_key)
        self.phonebook = Phonebook(api_key)
        self.campaign = Campaign(api_key)
        self.token = Token(api_key)
        self.insight = Insight(api_key)
