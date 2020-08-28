import requests
import discord
from discord.ext import commands

TOKEN = ''

description = '''Wallpapers_Abyss in Python | Gets our wallpaper from https://wall.alphacoders.com/'''

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """Says world"""
    await ctx.send("world")

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def search(ctx, search):
    """Search with word the wallpaper for multiple words put \"\" ex : !search \"Batman and Robin\""""
    await ctx.send(Search_Wallpaper(search))

def Search_Wallpaper(search):
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=search&term='+search)
    request_json = request.json()
    for p in request_json['wallpapers']:
        return p['url_image']
        break

@bot.command()
async def newest(ctx):
    """Get the newest Wallpaper"""
    await ctx.send(Newest_Wallpaper())

@bot.command()
async def random(ctx):
    """Get random Wallpaper"""
    await ctx.send(Random_Wallpaper())

def Newest_Wallpaper():
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=neweset')
    request_json = request.json()
    for p in request_json['wallpapers']:
        return p['url_image']
        break

def Random_Wallpaper():
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=random')
    request_json = request.json()
    for p in request_json['wallpapers']:
        return p['url_image']
        break

bot.run(TOKEN)
