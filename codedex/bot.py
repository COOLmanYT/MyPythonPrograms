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
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    if message.author == self.user:
      print('Ignoring self-message')
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
      print('Meme sent!')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(discord_token) # Replace with your own token.
