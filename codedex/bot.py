import discord
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')
if not discord_token: # Check if the token is missing.
  raise RuntimeError('DISCORD_TOKEN is missing. Check your .env file.')

def get_meme():
  response = requests.get('https://meme-api.com/gimme') # get meme from API.
  json_data = json.loads(response.text)
  return json_data['url'] # return meme URL.

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user)) # print a confirmation that bot is logged in

  async def on_message(self, message): # when a message is sent:
    if message.author == self.user:
      print('Ignoring self-message') # ignore messages sent by the bot
      return
    if message.content.startswith('$meme'): # if the message starts with $meme:
      await message.channel.send(get_meme()) # send the meme URL.
      print('Meme sent!') # print confirmation that meme was sent.

intents = discord.Intents.default()
intents.message_content = True # enable message content intent - check dev portal if it is enabled for the bot

client = MyClient(intents=intents)
client.run(discord_token) # run the bot
