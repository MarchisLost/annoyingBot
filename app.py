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
#youtube_dl.utils.bug_reports_message = lambda: ''

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
- Comandos para dar tag a pessoal de vários jogos, like !pummel ou !amongUs etc - DONE!
- meter estado do bot para !help e o help dizer pra perguntar ao sheep ou ao march
- Criar audit log num file que elimina apos +/- 30 dias
- Comando pra o mata kickar o bifes
"""

@client.event   
async def on_message(message):
    #Gets the user by its id - Necessary have one of this inside every event cuz if its outside it brakes cuz it happens before the client is created
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_GORDO')))
    mata = client.get_user(int(os.getenv('DISCORD_MATA')))
    bacon = client.get_user(int(os.getenv('DISCORD_BACON')))
    tiago = client.get_user(int(os.getenv('DISCORD_TIAGO'))) #aka sheeps best friend in the whole world kappa, nao apagues, e pro comando "clash" de lol
    fontes = client.get_user(int(os.getenv('DISCORD_FONTES')))
    #print(sheep, march)

    #Message Deleter-------
    if message.author == gordo:
        print('message author: ', message.author)
        await message.channel.purge(limit=1)

    #Commands to invite people for games -------------------------------------
    if message.content.startswith("!pummel"):
        print('pummel by: ', message.author)
        await message.channel.send('Sessão de pummel hoje?\n' + march.mention + ' ' + sheep.mention + ' ' + bacon.mention + ' ' + mata.mention)
    elif message.content.startswith("!r6"):
        print('r6 by: ', message.author)
        await message.channel.send('Alguém quer vir rainbow?\n Sheep Instala o rainbow!\n' + march.mention + ' ' + sheep.mention + ' ' + bacon.mention + ' ' + mata.mention + ' ' + fontes.mention)
    elif message.content.startswith("!amongus"):
        print('among us by: ', message.author)
        await message.channel.send('Sessão de Among Us?\n' + march.mention + ' ' + sheep.mention + ' ' + bacon.mention + ' ' + mata.mention + ' ' + fontes.mention)
    elif message.content.startswith("!clash"):
        print('clash by: ', message.author)
        await message.channel.send('Clash este fds? Alguém não pode?\n' + march.mention + ' ' + tiago.mention + ' ' + bacon.mention + ' ' + mata.mention + ' ' + fontes.mention)
    elif message.content.startswith("!help"):
        print('help by: ', message.author)
        await message.channel.send(march.mention + sheep.mention + '\nEsta aqui um nabo a pedir ajuda...\nPergunta a um destes dois se eles nao responderem!')
    elif message.content.startswith("!bifes"): #kicks bifes as mata requested
        print('bifes kicked by: ', message.author)
        for member in message.guild.members:
            if member.id == int("307621482186670082"): #bifes id
                bifes = member
        await bifes.kick(reason='You were being annoying dude, pls take it easy, thank you!')


#Disconnecter    
@client.event 
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    gordo = client.get_user(int(os.getenv('DISCORD_GORDO')))
    
    #Simple channel movements log 
    if before.channel is None:
        print(now, "-", member, "joined", after.channel)
    elif after.channel is None:
        print(now, "-", member, "left", before.channel)
    else:
        print(now, "-", member, "left", before.channel, "and joined", after.channel)
    
    #Disconnecting on specific user joining voice channels
    if member == gordo:
        print('member disconnected: ', member)
        await member.edit(voice_channel=None)
    
#Role remover - needs administrator role
@client.event 
async def on_member_update(before, after):
    #Stuff to remove later
    gordo = client.get_user(int(os.getenv('DISCORD_GORDO')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    
    #This is to check if someone on the hitlist changed roles
    #TODO "bitch" must be replaced with "Professor Chaos" on the other server
    sleep(5)
    if after == gordo or after == march and str(after.top_role) == "Professor Chaos":
        list_roles = after.roles.copy()
        
        #This is to check if professor chaos aka bitch is one of the roles and if it is, deletes it from the user
        for index, x in enumerate(list_roles, start=0):
            #Getting index of "bitch"
            if str(x) == "Professor Chaos":
                index_role = index
                del list_roles[index_role]
                await after.edit(roles=list_roles)
                print(after.roles)
                
client.run(TOKEN)