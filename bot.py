import discord
from discord.ext.commands import Bot
from modules.config import config

bot = Bot(command_prefix='>>>')

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.send_message(ctx.message.channel, "Pong!")

bot.run(config['token'])