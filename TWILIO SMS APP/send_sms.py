# First of all Open your terminal and install twilio by using the command `pip install twilio`.
# import these stuffs 
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio


client = TwilioRestClient(account_sid, auth_token)

my_msg = "Type your message here."

message = client.messages.create(to=my_cell, from_=my_twilio,body=my_msg)
                                     
