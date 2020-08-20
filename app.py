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

#Message Deleter
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

#Disconnecter    
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
    
#Role remover
@client.event 
async def on_member_update(before, after):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    #Stuff to remove later
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    
    #Print roles in log
    #print(now, "-", before.roles)
    #print(now, "-", after.top_role)
    
    #This is to check if someone on the hitlist changed roles
    #"bitch" must be replaced with "Professor Chaos" on the other server
    if after == gordo or after == sheep or after == march and str(after.top_role) == "bitch":
        list_roles = after.roles.copy()
        
        #This is to check if professor chaos aka bitch is one of the roles
        for index, x in enumerate(list_roles, start=0):
            #Getting index of "bitch"
            if str(x) == "bitch":
                index_role = index
                del list_roles[index_role]
                await after.edit(roles=list_roles)
                print(after.roles)
                break
        

client.run(TOKEN)