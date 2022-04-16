import discord
from discord.ext import commands
from to import Token
import math
from PIL import Image

bot=commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('login in prosess.')
    print(f"connecting to {bot.user.name}bot.")
    print('login is success.')
    await bot.change_presence(status=discord.Status.online, activity=None)
@bot.command(aliases=['hi']) #define command
async def hello(ctx): #this is command. you can change it.
    await ctx.send('hello.') #you can send message.
@bot.command()
async def followthewords(ctx,a):
    await ctx.send(a) #...or you can follow the messages.
bot.run(Token) #good luck!