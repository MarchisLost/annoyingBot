import os
import discord
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()


#TODO Requisitos para se fazer!
""" 
- Eliminar comentarios do gordo - DONE!
- Tirar lhe sempre a professor chaos
- Tirar lhe das salas
- Chatear o mata
- Criar permissoes nas salas para ele nem sequer conseguir entrar( not sure if this one works)
- Convinha que ele conseguisse reproduzir musicas do spotify e youtube para nao parecer que é totalmente inutil, provavelmente já há codigo disso por aí, não deve ser muito dificil - TRUE
- Criar comandos do tipo "annoy [user_id]" para podermos fazer as cenas on the fly
"""


@client.event
async def on_ready():
    print(f'{client.user} is connected!')
    #Gets servers that the bot is connected to
    print(client.guilds)

@client.event   
async def on_message(message):
    #Message Deleter-------
    #This is to be removed at a later stage, it's just for testing (basta tirar o sheep e march, o gordo fica ja)
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    if message.author == gordo or message.author == sheep or message.author == march:
        print(message.author)
        await message.channel.purge(limit=1)

    #TODO this can be deleted imo u choose tho
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#Disconnecter    
@client.event 
async def on_voice_state_update(member, before, after):
    now = datetime.now()
    timestamp = datetime.timestamp(now) #! este time e pra nao ser instantaneo tambem?
    
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
    timestamp = datetime.timestamp(now) #!!SHEEP Isto nao esta a ser usado, ainda vai ser usado pra nao se eliminar logo, right?
    
    #Stuff to remove later
    sheep = client.get_user(int(os.getenv('DISCORD_SHEEP')))
    march = client.get_user(int(os.getenv('DISCORD_MARCH')))
    gordo = client.get_user(int(os.getenv('DISCORD_USER')))
    
    #Print roles in log
    #print(now, "-", before.roles)
    #print(now, "-", after.top_role)
    
    #This is to check if someone on the hitlist changed roles
    #TODO "bitch" must be replaced with "Professor Chaos" on the other server
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

client.run(TOKEN)