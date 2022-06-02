import discord
from discord.ext import commands
import youtube_dl
import ffmpeg
import asyncio

# Mode d'emploi du bot musique
# Aller dans Voice Channels puis General
# Pour ecouter une musique ou vidéo mettre !play + url de la video "youtube" (dans la discution)
# Pour mettre pause !pause
# Pour reprendre la lecture !resume
# Pour tout stopper !skip


default_intents = discord.Intents.default()
default_intents.members = True
bot = discord.Client(intents=default_intents)


bot = commands.Bot(command_prefix="!", description="Bot pour tout le monde")
musics = {}
ytdl = youtube_dl.YoutubeDL()


@bot.event
async def on_member_join(member):
    general_channel: discord.TextChannel = bot.get_channel(token)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.mention} :)")


@bot.event
async def on_menber_remove(member):
    channel = bot.get_channel(token)
    await channel.send(f"merci de votre visite à biento {member.mention} :)")


@bot.event
async def on_ready():
    print("Ready")


class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]


@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []


@bot.command()
async def resume(ctx):
    client = ctx.guild.voice_client
    if client.is_paused():
        client.resume()


@bot.command()
async def pause(ctx):
    client = ctx.guild.voice_client
    if not client.is_paused():
        client.pause()


@bot.command()
async def skip(ctx):
    client = ctx.guild.voice_client
    client.stop()


def play_song(client, queue, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(
        song.stream_url, before_options="-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"))

    def next(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]
            play_song(client, queue, new_song)
        else:
            asyncio.run_coroutine_threadsafe(client.disconnect(), bot.loop)

    client.play(source, after=next)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client

    if client and client.channel:
        video = Video(url)
        musics[ctx.guild].append(video)
    else:
        channel = ctx.author.voice.channel
        video = Video(url)
        musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"je lance : {video.url}")
        play_song(client, musics[ctx.guild], video)


bot.run(token)
