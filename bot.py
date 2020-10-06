import requests
import key
import random
from disputils import BotEmbedPaginator, BotConfirmation, BotMultipleChoice
import discord
from discord.ext import commands

description = '''Wallpapers_Abyss in Python\r\nGets our wallpaper from https://wall.alphacoders.com/\r\nRepositorie : https://github.com/FehlmannDy/Bot_Discord_Wallpaper_Abyss\r\nAuthor : Dylan Fehlmann\r\nGitHub : https://github.com/FehlmannDy'''

bot = commands.Bot(command_prefix='!', description=description)

class Wallpaper:
    def __init__(self,id,url,file_type):
        self.id = id
        self.url= url
        self.file_type = file_type

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def Search(ctx, search):
    """Search with thema the wallpaper !search {"words"} ex: !search \"Batman and Robin\""""
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=search&term='+search)
    request_json = request.json()
    lWallpapers = []
    for picture in request_json['wallpapers']:
        w = Wallpaper(picture['id'],picture['url_image'],picture['file_type'])
        lWallpapers.append(w)
    
    random.shuffle(lWallpapers)
    e1=discord.Embed(title="The search "+search+" Wallpapers "+lWallpapers[0].id, color=0x115599)
    e1.set_image(url=lWallpapers[0].url)
    embeds = [e1]
    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()

@bot.command()
async def Newest(ctx):
    """Get the newest Wallpaper"""
    w = Newest_Wallpaper()
    e1=discord.Embed(title="The newest Wallpapers "+w.id, color=0x115599)
    e1.set_image(url=w.url)
    e1.set_footer(text=w.url)
    embeds = [e1]
    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()

def Newest_Wallpaper():
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=neweset')
    request_json = request.json()
    for picture in request_json['wallpapers']:
        return Wallpaper(picture['id'],picture['url_image'],picture['file_type'])
        break

@bot.command()
async def Random(ctx, many : int):
    """Get random Wallpaper !random {number} ex: !random 1"""
    if many is None:
        w = Random_Wallpaper()
        e1=discord.Embed(title="The random Wallpapers "+w.id, color=0x115599)
        e1.set_image(url=w.url)
        embeds = [e1]
    else:
        embeds = []
        for x in range(many):
            w = Random_Wallpaper()
            e1=discord.Embed(title="Wallpapers "+w.id, color=0x115599, image(url=w.url,width=600,height=800))
            e1.set_footer(text=w.url)
            embeds+=[e1]

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()

def Random_Wallpaper():
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=random')
    request_json = request.json()
    for picture in request_json["wallpapers"]:
        return Wallpaper(picture["id"],picture["url_image"],picture['file_type'])
        break

@bot.command()
async def Status(ctx):
    """Get number of request to this month"""
    month_count = Count_Request()
    last_month_count = Last_Month_Count_Request()
    e1=discord.Embed(title="Resquest of this month : {} / 150'000".format(month_count), color=0xF93A2F)
    e1.set_footer(text="Last month : {} / 150'000".format(last_month_count))
    await ctx.send(embed=e1)

def Count_Request():
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=query_count')
    request_json = request.json()
    return request_json['counts']['month_count']

def Last_Month_Count_Request():
    request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=query_count')
    request_json = request.json()
    return request_json['counts']['last_month_count']

bot.run(key.TOKEN)
