import discord
from discord.ext.commands import Bot
from modules.config import config

bot = Bot(command_prefix='>>>')

@bot.command()
async def ping(ctx):
    await ctx.channel.send("Pong!")
    
@bot.command(aliases=['md'])
async def markdown(ctx):
    await ctx.channel.send(("**Hey you!** Here is how you can use markdown syntax\n\n"
                        "\`\`\`py\n"
                        "print('Woah! Markdown helps me read your code :)')\n"
                        "\`\`\`\n\n"
                        "Will *magically* turn into this\n\n"
                        "```py\n"
                        "print('Woah! Markdown helps me read your code :)')\n"
                        "```")
                      )
@bot.command()
async def inlang(ctx, lang, *, code):
    await ctx.channel.send("```{0}\n{1}\n```".format(lang, code))

bot.run(config['token'])
