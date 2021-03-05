import config
import discord
import time
import asyncio
from discord.ext import commands, tasks

import mcipc.query


bot = commands.Bot(command_prefix=config.prefix,
                   intents=discord.Intents.default())


def get_status():
    try:
        pt = time.time()
        with mcipc.query.Client(config.host, config.port) as mcbe:
            status = mcbe.stats(full=True)
            ping = (time.time()-pt)*1000
        del mcbe
        return status, ping
    except:
        return None
    


@tasks.loop(seconds=30)
async def server_status_updater():
    await bot.wait_until_ready()
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, get_status)
    if not data:
        return await bot.change_presence(
            status=discord.Status.dnd, activity=discord.Game('サーバーがオフラインです'))
    st = f'{data[0].num_players} / {data[0].max_players} | ping: {data[1]:.1f}ms'
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game(st))


@bot.event
async def on_ready():
    server_status_updater.start()
    print('準備ができました')

bot.run(config.bot_token)
