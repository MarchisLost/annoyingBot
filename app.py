import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} is connected!')
    #Gets servers that the bot is connected to
    print(client.guilds)

#Gets fat jonny id
#gordo = client.get_user(524276962106146838)
#print('gordo:', gordo)

@client.event   
async def on_message(message):
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    print(gordo)
    if message.author == gordo:
        await message.channel.purge(limit=1)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)