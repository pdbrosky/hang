import os
from twilio.rest import Client

cwd = os.getcwd()

with open(cwd+'/auth/twilio_sid') as file:
    sid = file.read()

with open(cwd+'/auth/twilio_token') as file:
    token = file.read()

account_sid = sid
auth_token = token
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello world!',
                              from_='+19083567484',
                              to='+19084871576'
                          )

print(message.sid)
