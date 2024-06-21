'''SMS connection to Twilio API'''

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

def send_message(message: str, sender='+18777194154', receiver='+18187952054'): 
    client = twilio_connection()
     
    message = client.messages \
                        .create(
                            body = message, 
                            from_=sender, 
                            to=receiver
                        )
    if not message.sid: 
        return False
    return message.sid

def send_image(message: str, sender='+18777194154', receiver='+18187952054'): 
    client = twilio_connection()
     
    message = client.messages \
                        .create(
                            body = message, 
                            from_=sender, 
                            to=receiver
                        )
    if not message.sid: 
        return False
    return message.sid

def send_object(message: str, sender='+18777194154', receiver='+18187952054'): 
    client = twilio_connection()
     
    message = client.messages \
                        .create(
                            body = message, 
                            from_=sender, 
                            to=receiver
                        )
    if not message.sid: 
        return False
    return message.sid
