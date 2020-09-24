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

# Silence useless bug reports messages
#youtube_dl.utils.bug_reports_message = lambda: ''
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
# Gets user id's
sheep = int(os.getenv('DISCORD_SHEEP'))
march = int(os.getenv('DISCORD_MARCH'))
gordo = int(os.getenv('DISCORD_GORDO'))
mata = int(os.getenv('DISCORD_MATA'))
bacon = int(os.getenv('DISCORD_BACON'))
tiago = int(os.getenv('DISCORD_TIAGO')) #aka sheeps best friend in the whole world kappa, nao apagues, e pro comando "clash" de lol
fontes = int(os.getenv('DISCORD_FONTES'))
    #print(sheep, march)
bot = commands.Bot(command_prefix='!')

#TODO Requisitos para se fazer!
""" 
- Eliminar comentarios do gordo - DONE!
- Tirar lhe sempre a professor chaos - DONE!
- Tirar lhe das salas - DONE!
- Chatear o mata
- Criar permissoes nas salas para ele nem sequer conseguir entrar( not sure if this one works)
- Convinha que ele conseguisse reproduzir musicas do spotify e youtube para nao parecer que é totalmente inutil - IN PROGRESS, STILL VERY SCUFFED
- Criar comandos do tipo "annoy [user_id]" para podermos fazer as cenas on the fly
- Comandos para dar tag a pessoal de vários jogos, like !pummel ou !amongUs etc - DONE!
- meter estado do bot para !help e o help dizer pra perguntar ao sheep ou ao march
- Criar audit log num file que elimina apos +/- 30 dias
- Comando pra o mata kickar o bifes
"""

@bot.command()
async def test(ctx):
    await ctx.send("123")

#Commands to invite people for games -------------------------------------
@bot.command()
async def pummel(ctx):
    print('pummel by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Sessão de pummel hoje?\n' + bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention)

@bot.command()
async def r6(ctx):
    print('r6 by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Alguém quer vir rainbow?\n Sheep Instala o rainbow!\n' + bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention + ' ' + bot.get_user(fontes).mention)

@bot.command()
async def amongus(ctx):
    print('among us by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Sessão de Among Us?\n' + bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention + ' ' + bot.get_user(fontes).mention)
        
@bot.command()
async def clash(ctx):
    print('clash by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Clash este fds? Alguém não pode?\n' + bot.get_user(march).mention + ' ' + bot.get_user(tiago).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention + ' ' + bot.get_user(fontes).mention)

@bot.command()
async def bifes(ctx):
    print('bifes kicked by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    for member in ctx.guild.members:
        if member.id == int("307621482186670082"): #bifes id
            bifes = member
    await bifes.kick(reason='You were being annoying dude, pls take it easy, thank you!')

""" Existe uma cena própria para o comando help, temos de usar isso em vez disto
elif message.content.startswith("!help"):
    print('help by: ', message.author)
    await message.channel.send(bot.get_user(march).mention + bot.get_user(sheep).mention + '\nEsta aqui um nabo a pedir ajuda...\nPergunta a um destes dois se eles nao responderem!')
"""

@bot.event   
async def on_message(message):
    #Message Deleter-------
    if message.author == bot.get_user(gordo):
        print('message author: ', message.author)
        await message.channel.purge(limit=1)
    await bot.process_commands(message)

#Disconnecter    
@bot.event 
async def on_voice_state_update(member, before, after):
    now = datetime.now()   
    #Simple channel movements log 
    if before.channel is None:
        print(now, "-", member, "joined", after.channel)
    elif after.channel is None:
        print(now, "-", member, "left", before.channel)
    else:
        print(now, "-", member, "left", before.channel, "and joined", after.channel)
    
    #Disconnecting on specific user joining voice channels
    if member == bot.get_user(gordo):
        print('member disconnected: ', member)
        await member.edit(voice_channel=None)
    
#Role remover - needs administrator role
@bot.event 
async def on_member_update(before, after):
    #This is to check if someone on the hitlist changed roles
    sleep(5)
    if after == bot.get_user(gordo) and str(after.top_role) == "Professor Chaos":
        list_roles = after.roles.copy()
        
        #This is to check if professor chaos aka bitch is one of the roles and if it is, deletes it from the user
        for index, x in enumerate(list_roles, start=0):
            #Getting index of "bitch"
            if str(x) == "Professor Chaos":
                index_role = index
                del list_roles[index_role]
                await after.edit(roles=list_roles)
                print(after.roles)
                
@bot.event
async def on_ready():
    print(f'{bot.user} is connected!')
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    #Gets servers that the bot is connected to
    print(bot.guilds)
bot.run(TOKEN)