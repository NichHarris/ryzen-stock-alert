import twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC0f3243186875bd7d009d16229b31cea3"
# Your Auth Token from twilio.com/console
auth_token  = "c48189e21f517f9ec92d4201a557d85c"

client = Client(account_sid, auth_token)
link = "X"
message = client.messages.create(
    to="+14388327376", 
    from_="+12184927786",
    body="RYZEN 5600X LINK: " + link)

print(message.sid)