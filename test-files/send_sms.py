import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
myNum = os.environ['MY_NUM']
twilioNum = os.environ['TWILIO_NUMBER']

client = Client(account_sid, auth_token)
link = "X"

message = client.messages.create(to=myNum, from_=twilioNum, body="RYZEN 5600X LINK: {}".format(link))

print(message.sid)