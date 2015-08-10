import os
from os.path import join, dirname

from twilio.rest import TwilioRestClient 
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

auth = os.environ.get('TWILIO_SID')
token = os.environ.get('TWILIO_SECRET')
to_phone = os.environ.get('TO_PHONE')
from_phone = os.environ.get('FROM_PHONE')

msg = 'this is a test'

client = TwilioRestClient(auth,token)  
msg = client.messages.create(to=to_phone, from_=from_phone, body=msg)