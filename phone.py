import random, schedule, time

from twilio.rest import Client

GOOD_MORNING_QUOTES = [
    "You're so funny!", 
    "Have a great day!", 
    "Good morning"
]

cellphone = 6132550283
twilio_number = 14243040460

def send_message(quote):
  account = "AC88836d435a54160ccc96afd91d2a5f02"
  token = "d4ec6f9a7df9ad1a8927308d110077b6"
  client = Client (account,token)
  client.messages.create(to=cellphone,from=twilio_number,body=quote)

quote = GOOD_MORNING_QUOTES[random.randint(0,len(GOOD_MORNING_QUOTES))]
schedule.every().day.at("6:30").do(send_message,GOOD_MORNING_QUOTES[0])
