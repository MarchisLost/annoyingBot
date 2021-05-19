import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import random
import re
import logging

# TTS
import pyttsx3

# This one is to get current time
import time
from musicbot.music import Music

from datetime import date
today = date.today()


# Declaring intents
intents = discord.Intents.all()

d1 = str(today.strftime("%Y-%m-%d"))
log_name = 'logs/' + d1 + '.log'

logging.basicConfig(filename=log_name, format='%(asctime)s - %(name)s \
- %(levelname)s - %(message)s', level=logging.DEBUG)

# create logger
logger = logging.getLogger('Watchdog')
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s'
                              '- %(name)s'
                              '- %(levelname)s'
                              '- %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

""" Available ways to log files """
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

# This gets the pid of the bots process and stores it into a file so it read and then be killed on the automation script
pid = os.getpid()
with open('logs/pid/pid.txt', 'w') as pidFile:
    pidFile.write(str(pid))
    print(pid)

# Necessário para o código funcionar no Spyder e noutros IDE's
# import nest_asyncio
# nest_asyncio.apply()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# Gets user id's
sheep = int(os.getenv('DISCORD_SHEEP'))
march = int(os.getenv('DISCORD_MARCH'))
gordo = int(os.getenv('DISCORD_GORDO'))
mata = int(os.getenv('DISCORD_MATA'))
bacon = int(os.getenv('DISCORD_BACON'))
tiago = int(os.getenv('DISCORD_TIAGO'))
fontes = int(os.getenv('DISCORD_FONTES'))
tomas = int(os.getenv('DISCORD_TOMAS'))
vera = int(os.getenv('DISCORD_VERA'))
tiagoULP = int(os.getenv('DISCORD_TIAGO_ULP'))

# Gets the image path
img_path = 'tsm.jpeg'
pfp = open(img_path, 'rb')
img = pfp.read()

pl_id = 'spotify:playlist:1Qhy7QA5Gfgc1Ugwpk5iXl'

songList = []
playlistName = ""


confirmed = 0
max_players_pummel = 8

voice_client = ''


# Getting current time in miliseconds
def current_milli_time():
    return round(time.time() * 1000)


# Created the bot with a prefix
bot = commands.Bot(command_prefix='!',
                   description="Discord bot created by March & Sheep",
                   intents=intents)

# Removes the default help command so we can create a new one
bot.remove_command('help')


@bot.command()
async def test(ctx):
    logger.info("%s -> %s", ctx.author.name, ctx.message.content)
    await ctx.send("123")


# Commands to invite people for games -------------------------------------
# Universal One
@bot.command(name='invite', aliases=['inv'])
async def invite(ctx, role):
    logger.info("%s invited to %s", ctx.author.name, role)
    await ctx.channel.purge(limit=1)
    # print(str(role))
    role = int(re.sub(r'\D', '', role))
    # print(str(role))
    role = ctx.guild.get_role(role)
    logger.info("Invitation to play %s by ctx.author.name", role.name)
    global max_players_pummel
    # confirmed = 0
    # Create embed
    embed_var = discord.Embed(title="Sessão de "
                                    + role.name
                                    + " hoje?",
                              description=" ",
                              color=role.colour)
    members = role.members

    # Next 2 lines are to tag the members of that role
    for x in members:
        logger.info('Invited %s', x.name)
        embed_var.add_field(name=x.name, value=x.mention, inline=False)

    # After the embeb is created this reacts with the 2 emojis of yay or nay
    mess = await ctx.channel.send(embed=embed_var)
    await mess.add_reaction("✅")
    await mess.add_reaction("❎")


# Command to kick bifes - change to be able to kick @someone
@bot.command()
async def bifes(ctx):
    logger.info("%s -> %s", ctx.author.name, ctx.message.content)
    print('bifes kicked by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    for member in ctx.guild.members:
        if member.id == int("307621482186670082"):  # bifes id
            bifes_m = member
            await bifes_m.kick(reason='You were being annoying dude, '
                                      'pls take it easy, thank you!')


# New help command
@bot.command()
async def help(ctx):
    logger.info("%s -> %s", ctx.author.name, ctx.message.content)
    print('help by: ', ctx.author)
    await ctx.channel.send(bot.get_user(march).mention
                           + ' ' + bot.get_user(sheep).mention
                           + '\nEsta aqui um nabo a pedir ajuda...'
                           '\nPergunta a um destes dois se eles nao responderem!'
                           '\nPara a musica é so !play song name/spotify link'
                           '\n Para jogos é so !invite @role')


# Deletes Gordo's messages
@bot.event
async def on_message(message):
    if not message.guild:
        # Hidden feature, send !r {sentence} in a DM for the bot to read out the {sentence}
        # Only in DM's
        if message.content.startswith('!r'):
            global voice_client
            guild = bot.guilds[0]
            if not voice_client:
                for vc in guild.voice_channels:
                    for member in vc.members:
                        if member.id == message.author.id:
                            voice_client = await vc.connect()
                            engine = pyttsx3.init()
                            engine.save_to_file(message.content[3:], 'test.mp3')
                            engine.runAndWait()
                            audio_source = discord.FFmpegPCMAudio("test.mp3")
                            voice_client.play(audio_source, after=None)
            else:
                engine = pyttsx3.init()
                engine.save_to_file(message.content[3:], 'test.mp3')
                engine.runAndWait()
                audio_source = discord.FFmpegPCMAudio("test.mp3")
                voice_client.play(audio_source, after=None)
    # Message Deleter-------
    if message.author != bot.user:
        logger.info("%s said -> %s", message.author.name, message.content)
    if message.author == bot.get_user(gordo):
        logger.info("Deleted %s's message -> [%s]", message.author.name, message.content)
        await message.channel.purge(limit=1)
    await bot.process_commands(message)
    # Annoy mata everytime he writes something
    if message.author == bot.get_user(mata):
        num = random.random() * 100
        # print(num)
        if num >= 50:
            await message.add_reaction('🖕')
        elif num < 10:
            choice = await message.channel.send(message.author.mention + " " + random.choice(mensagem))
            logger.info("said [%s] to mata", str(choice))

mensagem = ["You're a bitch",
            "No you",
            "Já estou farto de te ouvir bitch",
            "Vai estudar!",
            "A tua mãe chamou-te",
            "Celtics suck!",
            "Ouvi dizer que o Sheep te insultou",
            "Ouvi dizer que o March te insultou",
            "U gay",
            "Roses are red, violets are blue, I've got five fingers and the middle one is for you ;)",
            "If you were a vegetable you'd be a cabbitch",
            "So if i typed 'idiot' into Google would your picture come up?"]


# Functions that get the user reations (yay or nay) and changes the emebeb to display their answers
async def embed_yes(payload):
    global max_players_pummel
    channel = bot.get_channel(payload.channel_id)
    msg = await channel.fetch_message(payload.message_id)
    embed = msg.embeds[0]
    embed_dic = embed.to_dict()
    fields = embed_dic.get('fields')
    id_user = ""
    index = 0
    # print(payload.user_id)
    for ind, x in enumerate(fields):
        id_field = re.sub(r'\D', '', x['value'])
        # print(id_field)
        if int(id_field) == payload.user_id:
            id_user = int(id_field)
            index = ind
    user = bot.get_user(id_user)
    nome = user.name
    print(nome)
    print(id_user)
    print(index)
    nome += " ✅"
    # print(user.name)
    embed.set_field_at(index, name=nome, value=user.mention, inline=False)
    embed_dic = embed.to_dict()
    fields = embed_dic.get('fields')
    confirmed_1 = 0
    for x in fields:
        if "✅" in str(x['name']):
            confirmed_1 += + 1
    await msg.edit(embed=embed)
    print("check marked")


# Stuff about among us
async def embed_no(payload):
    channel = bot.get_channel(payload.channel_id)
    msg = await channel.fetch_message(payload.message_id)
    embed = msg.embeds[0]
    embed_dic = embed.to_dict()
    fields = embed_dic.get('fields')
    id_user = ""
    index = 0
    # print(payload.user_id)
    for ind, x in enumerate(fields):
        id_field = re.sub(r'\D', '', x['value'])
        # print(id_field)
        if int(id_field) == payload.user_id:
            id_user = int(id_field)
            index = ind
    user = bot.get_user(id_user)
    nome = user.name
    print(nome)
    print(id_user)
    print(index)
    nome += " ❎"
    # print(user.name)
    embed.set_field_at(index, name=nome, value=user.mention, inline=False)
    embed_dic = embed.to_dict()
    fields = embed_dic.get('fields')
    confirmed_1 = 0
    for x in fields:
        if "✅" in str(x['name']):
            confirmed_1 += + 1
    await msg.edit(embed=embed)
    print("cross marked")


# Stuff about among us nr of players maybe?
@bot.event   
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == "✅" and payload.user_id != bot.user.id:
        logger.info("User %s said Yes", bot.get_user(payload.user_id).name)
        await embed_yes(payload)

    elif str(payload.emoji) == "❎" and payload.user_id != bot.user.id:
        logger.info("User %s said No", bot.get_user(payload.user_id).name)
        await embed_no(payload)

    elif payload.user_id != bot.get_user(gordo) and payload.user_id != bot.user.id:
        channel = bot.get_channel(payload.channel_id)
        msg = await channel.fetch_message(payload.message_id)
        logger.info("Copied %s's reaction", bot.get_user(payload.user_id).name)
        await msg.add_reaction(payload.emoji)


# Stuff for the among us nr of players
@bot.event  
async def on_raw_reaction_remove(payload):
    global max_players_pummel
    if str(payload.emoji) == "✅" and payload.user_id != bot.user.id:
        logger.info("User %s removed Yes", bot.get_user(payload.user_id).name)
        await embed_yes(payload)

    elif str(payload.emoji) == "❎" and payload.user_id != bot.user.id:
        logger.info("User %s removed No", bot.get_user(payload.user_id).name)
        await embed_no(payload)


last_time = current_milli_time()
mute_count = 0


# Disconnectes Gordo from voice channels
@bot.event
async def on_voice_state_update(member, before, after):
    global last_time  # This is global so i can use it to check the time between mutes
    global mute_count
    # Simple channel movements log
    if before.self_mute != after.self_mute:
        current_time = current_milli_time()
        print(last_time)
        print(current_time)
        print(current_time - last_time)
        if current_time - last_time < 500:
            mute_count += 1
        else:
            mute_count = 0
        if mute_count > 3:
            voice_client = await after.channel.connect()
            mute_count = 0
            engine = pyttsx3.init()
            engine.save_to_file("march is a bitch", 'test.mp3')
            engine.runAndWait()
            audio_source = discord.FFmpegPCMAudio("test.mp3")
            await voice_client.play(audio_source, after=None)
        last_time = current_time
    elif before.channel is None:
        logger.info("%s joined %s", member, after.channel)
    elif after.channel is None:
        logger.info("%s left %s", member, before.channel)
    else:
        logger.info("%s left %s and joined %s", member, before.channel, after.channel)

    # Disconnecting on specific user joining voice channels
    if member == bot.get_user(gordo):
        logger.info('member disconnected: ', member)
        await member.edit(voice_channel=None)


# Removes Gordo's Professor chaos role- needs administrator role
@bot.event
async def on_member_update(before, after):
    if str(before.activity) != str(after.activity):
        logger.info("%s current activity changed to: '%s'", before.name, str(after.activity))
    """Isto deteta se alguém mudou de status"""
    if str(before.status) != str(after.status):
        logger.info("%s current status changed to:'%s'", before.name, str(after.status))
    """Isto deteta se alguém mudou o nickname"""
    if before.nick != after.nick:
        # Aqui é para ver se a pessoa já tinha um nickname \
        #  para não dar None quando se tenta escrever o nome na mensagem de info
        if before.nick:
            name_1 = before.nick
        else:
            name_1 = before.name
        if after.nick:
            name_2 = after.nick
        else:
            name_2 = after.name
        logger.info("%s changed nickname to:'%s'", name_1, name_2)

    """Isto deteta se alguém mudou de roles"""
    if before.roles != after.roles:
        # This is to check if someone on the hitlist changed roles
        logger.info("%s changed roles", after.name)
        if after == bot.get_user(gordo) and str(after.top_role) == "Professor Chaos":
            list_roles = after.roles.copy()
            # This is to check if professor chaos aka bitch is one of the roles and if it is, deletes it from the user
            for index, x in enumerate(list_roles, start=0):
                # Getting index of "bitch"
                if str(x) == "Professor Chaos":
                    index_role = index
                    del list_roles[index_role]
                    await after.edit(roles=list_roles)
                    # print(after.roles)

# Music bot
bot.add_cog(Music(bot))


@bot.event
async def on_ready():
    # Changes bot status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                        name='You !help if you dumb enough\n'
                                                        'Created by March & Sheep'))
    # await bot.user.edit(avatar=img)
    print(f'{bot.user} is connected!')
    print('Logged in as: {0.user.name}'.format(bot))
    print('Connected on the following servers:')
    # Gets servers that the bot is connected to
    for i in range(len(bot.guilds)):
        print('  ', bot.guilds[i].name)
    logger.info('Bot started')

bot.run(TOKEN)
