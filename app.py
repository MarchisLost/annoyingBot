import os
import discord
from discord.ext import commands
from time import sleep
from dotenv import load_dotenv
from datetime import datetime

import asyncio
import functools
import itertools
import math
import random

import youtube_dl
from async_timeout import timeout

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

#TODO Requisitos para se fazer!
""" 
- Eliminar comentarios do gordo - DONE!
- Tirar lhe sempre a professor chaos
- Tirar lhe das salas - DONE!
- Chatear o mata
- Criar permissoes nas salas para ele nem sequer conseguir entrar( not sure if this one works)
- Convinha que ele conseguisse reproduzir musicas do spotify e youtube para nao parecer que é totalmente inutil, provavelmente já há codigo disso por aí, não deve ser muito dificil - TRUE
- Criar comandos do tipo "annoy [user_id]" para podermos fazer as cenas on the fly
- Comandos para dar tag a pessoal de vários jogos, like !pummel ou !amongUs etc
"""

#This is to be removed at a later stage, it's just for testing (basta tirar o sheep e march, o gordo fica ja)
sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
march = client.get_user(int(os.getenv('DISCORD_MARCH')))
gordo = client.get_user(int(os.getenv('DISCORD_GORDO')))
mata = client.get_user(int(os.getenv('DISCORD_MATA')))
bacon = client.get_user(int(os.getenv('DISCORD_BACON')))
tiago = client.get_user(int(os.getenv('DISCORD_TIAGO'))) #aka sheeps best friend in the whole world kappa, nao apagues, e pro comando "clash" de lol
fontes = client.get_user(int(os.getenv('DISCORD_FONTES')))

@client.event   
async def on_message(message):
    #Message Deleter-------
    
    if message.author == gordo or message.author == march:
        print('message author: ', message.author)
        await message.channel.purge(limit=1)

    #Commands to invite people for games -----------------------------------------------------
    channel = message.channel
    print('channel:', channel)
    if message.content.startswith("!pummel"):
        print('pummel')
        #await channel.send('pummel here')
        #await channel.send('%s is the best ' % march)
    elif message.content.startswith == "!r6":
        pass
    elif message.content.startswith == "!amongus":
        pass
    elif message.content.startswith == "!clash":
        pass


#Disconnecter    
@client.event 
async def on_voice_state_update(member, before, after):
    now = datetime.now()
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
    if member == gordo or member == march:
        print('member disconnected: ',member)
        await member.edit(voice_channel=None)
    
#Role remover
@client.event 
async def on_member_update(before, after):
    #Stuff to remove later
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    
    #This is to check if someone on the hitlist changed roles
    #TODO "bitch" must be replaced with "Professor Chaos" on the other server
    sleep(5)
    if after == gordo or after == sheep or after == march and str(after.top_role) == "bitch":
        list_roles = after.roles.copy()
        
        #This is to check if professor chaos aka bitch is one of the roles and if it is, deletes it from the user
        for index, x in enumerate(list_roles, start=0):
            #Getting index of "bitch"
            if str(x) == "bitch":
                index_role = index
                del list_roles[index_role]
                await after.edit(roles=list_roles)
                print(after.roles)
                

#Commands to invite people for games
""" bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def sendMessage(ctx):
     """


client.run(TOKEN)