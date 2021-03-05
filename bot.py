import config
import discord
import time
from discord.ext import commands, tasks

import mcipc.query

bot = commands.Bot(command_prefix=config.prefix, intents=discord.Intents.default())

@tasks.loop(seconds=30)
async def server_status_updater():
  
  status = None
  
  try:
    pt = time.time()
    with mcipc.query.Client(config.host, config.port) as mcbe:
      status = mcbe.stats(full=True)
      ping = (time.time()-pt)*1000
      
  except:
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('サーバーがオフラインです'))
    return
  
  st = f'{status.num_players} / {status.max_players} | ping: {ping:.1f}ms'
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(st))

@bot.event
async def on_ready():
  
  server_status_updater.start()
  
  print('準備ができました')
  
bot.run(config.bot_token)