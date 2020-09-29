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

from async_timeout import timeout
import youtube_dl

import spotify

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
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

#Gets the image path
img_path = 'tsm.jpeg'
pfp = open(img_path, 'rb')
img = pfp.read()

pl_id = 'spotify:playlist:1Qhy7QA5Gfgc1Ugwpk5iXl'

songList = []
playlistName = ""

#Created the bot with a prefix
bot = commands.Bot(command_prefix='!', description="Discord bot created by March & Sheep")
bot.remove_command('help') #Removes the default help command so we can create a new one

@bot.command()
async def test(ctx):
    await ctx.send("123")
    songList = spotify.getSongs(pl_id)
    for x in songList:
        print(x) 

#Commands to invite people for games -------------------------------------
#Pummel Party
@bot.command()
async def pummel(ctx):
    print('pummel by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Sessão de pummel hoje?\n' + bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention)

#Rainbow Six Siege
@bot.command()
async def r6(ctx):
    print('r6 by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Alguém quer vir rainbow?\n Sheep Instala o rainbow!\n' + bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention + ' ' + bot.get_user(fontes).mention)

#Among Us
@bot.command()
async def amongus(ctx):
    print('among us by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Sessão de Among Us?\n' + bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention + ' ' + bot.get_user(fontes).mention + ' ' + bot.get_user(tomas).mention + ' ' + bot.get_user(vera).mention + ' ' + bot.get_user(tiagoULP).mention)

#Clash - Lol        
@bot.command()
async def clash(ctx):
    print('clash by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    await ctx.channel.send('Clash este fds? Alguém não pode?\n' + bot.get_user(march).mention + ' ' + bot.get_user(tiago).mention + ' ' + bot.get_user(bacon).mention + ' ' + bot.get_user(mata).mention + ' ' + bot.get_user(fontes).mention)
#Ended  --  Commands to invite people for games -------------------------------------

#Comand to kick bifes - change to be able to kick @someone
@bot.command()
async def bifes(ctx):
    print('bifes kicked by: ', ctx.author)
    await ctx.channel.purge(limit=1)
    for member in ctx.guild.members:
        if member.id == int("307621482186670082"): #bifes id
            bifes = member
    await bifes.kick(reason='You were being annoying dude, pls take it easy, thank you!')

#New help command
@bot.command()
async def help(ctx):
    print('help by: ', ctx.author)
    await ctx.channel.send(bot.get_user(march).mention + ' ' + bot.get_user(sheep).mention + '\nEsta aqui um nabo a pedir ajuda...\nPergunta a um destes dois se eles nao responderem!\nPara a musica é so !play song name/spotify link')


#Deletes Gordo's messages
@bot.event   
async def on_message(message):
    #Message Deleter-------
    if message.author == bot.get_user(gordo):
        print('message author: ', message.author)
        await message.channel.purge(limit=1)
    await bot.process_commands(message)
    if message.author == bot.get_user(mata):
        num = random.random() * 100
        #print(num)
        if num >= 50:
            await message.add_reaction('🖕')
        elif num < 10:
            await message.channel.send(message.author.mention + " " + random.choice(mensagem))
        
        
mensagem = ["You're still a bitch tho ", "No you", "Já estou farto de te ouvir bitch", "Vai estudar!", "A tua mãe chamou-te", "Os teus Celtics são uma porcaria!", "Ouvi dizer que o Sheep te insultou", "Ouvi dizer que o March te insultou", "U gay","My middle finger get's a boner when i think of you ;)", "Roses are red, violets are blue, I've got five fingers and the middle one is for you ;)", "Life is short and so is your penis.", "You are cordially invited to Go Fuck Yourself :D"]

#Disconnectes Gordo from voice channels
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
  
#Removes Gordo's Professor chaos role- needs administrator role
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

# MUSIC BOT

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(discord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: discord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, discord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (discord.Embed(title='Now playing',
                               description='{0.source.title}'.format(self),
                               color=discord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_footer(text="btw, mata's a bitch")
                 .set_thumbnail(url=self.source.thumbnail))
        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, client: commands.Bot, ctx: commands.Context):
        self.client = client
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = client.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.client.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))
        songList.pop(0)
        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.client, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.client.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='summon')
    @commands.has_permissions(manage_guild=True)
    async def _summon(self, ctx: commands.Context, *, channel: discord.VoiceChannel = None):
        """Summons the client to a voice channel.

        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()

    @commands.command(name='leave', aliases=['disconnect'])
    @commands.has_permissions(manage_guild=True)
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.message.add_reaction(':wave:')
        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    @commands.has_permissions(manage_guild=True)
    async def _pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='resume')
    @commands.has_permissions(manage_guild=True)
    async def _resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if not ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')

    @commands.command(name='stop')
    @commands.has_permissions(manage_guild=True)
    async def _stop(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        ctx.voice_state.songs.clear()

        if not ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')

        """  COM VOTES
        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))
                
        else:
            await ctx.send('You have already voted to skip this song.')
        """


        # SEM VOTES
        await ctx.message.add_reaction('⏭')
        ctx.voice_state.skip()
        
    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.

        You can optionally specify the page to show. Each page contains 10 elements.
        """
        global songList
        global playlistName
        
        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        await ctx.message.add_reaction('✅')
        items_per_page = 10
        pages = math.ceil(len(songList) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(songList[start:end], start=start):
            queue += "%s - %s \n" % (i+1, song)
        print(playlistName)
        embed = (discord.Embed(description='**{} tracks:**\n\n{}'.format(len(songList), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        random.shuffle(songList)
        ctx.voice_state.songs.clear()
        await ctx.message.add_reaction('🔀')
        print(songList)
        for x in songList:
                search = x     
                try:
                    source = await YTDLSource.create_source(ctx, search, loop=self.client.loop)
                except YTDLError as e:
                    await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
                else:
                    song = Song(source)
                    await ctx.voice_state.songs.put(song)

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """Loops the currently playing song.

        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.

        If there are songs in the queue, this will be queued until the
        other songs finished playing.

        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        
        """
        global songList
        global playlistName
        
        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)
        
        await ctx.message.add_reaction('✅')
        txt = str(search)
        songList1 = []
        if (txt.__contains__('spotify')):
            try:
                songList1, playlistName = spotify.getSongs(txt)
                songList.extend(songList1)
                await ctx.send('Enqueued ' + str(len(songList)) + ' songs!')
            except:
                songList1, playlistName = spotify.getSongs(pl_id)
                songList.extend(songList1)
                await ctx.send('I did not find the music/playlist you requested, in the mean time listen to this one made by my daddy!')
            
            for x in songList:
                search = x     
                try:
                    source = await YTDLSource.create_source(ctx, search, loop=self.client.loop)
                except YTDLError as e:
                    await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
                else:
                    song = Song(source)
                    await ctx.voice_state.songs.put(song)
        else:

            async with ctx.typing():
                try:
                    source = await YTDLSource.create_source(ctx, search, loop=self.client.loop)
                except YTDLError as e:
                    await ctx.send('An error occurred while processing this request: {}'.format(str(e)))
                else:
                    song = Song(source)
                    await ctx.voice_state.songs.put(song)
                    await ctx.send('Enqueued {}'.format(str(source)))

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')



bot.add_cog(Music(bot))

#      
@bot.event
async def on_ready():
    #Changes bot status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='You !help if you dumb enough\nCreated by March & Sheep'))
    #await bot.user.edit(avatar=img)
    print(f'{bot.user} is connected!')
    print('Logged in as: {0.user.name}'.format(bot))
    print('Connected on the following servers:')
    #Gets servers that the bot is connected to
    for i in range(len(bot.guilds)):
        print('  ', bot.guilds[i].name)
    
bot.run(TOKEN)