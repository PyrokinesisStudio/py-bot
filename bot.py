import discord
from discord.ext.commands import Bot
from modules.config import config

bot = Bot(command_prefix='>>>')

@bot.command()
async def ping(ctx):
    await channel.send("Pong!")

bot.run(config['token'])