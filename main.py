import discord
from discord.ext import commands

TOKEN = "OTk3MzQzODcwMzA2MjQyNjEw.GUkOIz.UDa8I-CjsDdFyd9oxeuFnrYUYrHVHRq22g-kJ4"

intents = discord.Intents.default()
intents.message_content = True # Enable the bot to see messages and commands
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command() # bot, please register this method as a command
async def hello(ctx):
    await ctx.channel.send("world!")

@bot.command()
async def goodbye(ctx):
    await ctx.channel.send("world!")

@bot.event # bot, please register this method as an event
async def on_ready():
    print("Our bot is ready to go!")

bot.run(TOKEN)

#####

# Main Page: https://discordpy.readthedocs.io/en/latest/
# API Docs: https://discordpy.readthedocs.io/en/latest/api.html