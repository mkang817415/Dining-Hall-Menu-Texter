'''Whatsapp connection to Twilio API'''

import os
import sys
from dotenv import load_dotenv

from twilio.rest import Client

sys.path.append('../')


def twilio_connection(): 
    load_dotenv() 
    
    # Gathering Credentials
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    return client 