import os

import discord
from dotenv import load_dotenv
from datetime import datetime

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
    
    #This is to be removed at a later stage, it's just for testing
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    #print(gordo)
    if message.author == gordo or message.author == sheep or message.author == march:
        print(message.author)
        await message.channel.purge(limit=1)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
@client.event 
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    #Stuff to remove later
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    
    #Simple channel movements log 
    if before.channel is None:
        print(now, "-", member, "joined", after.channel)
    elif after.channel is None:
        print(now, "-", member, "left", before.channel)
    else:
        print(now, "-", member, "left", before.channel, "and joined", after.channel)
    
    #Disconnecting on specific user joining voice channels
    if member == gordo or member == sheep or member == march:
        await member.edit(voice_channel=None)
    
    
client.run(TOKEN)