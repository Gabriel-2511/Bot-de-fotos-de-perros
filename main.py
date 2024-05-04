import discord
from discord.ext import commands
import os, random

print(os.listdir ("M2L1\perros"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

@bot.command()
async def dog(ctx):
    img_name = random.choice(os.listdir("M2L1\perros"))
    with open(f'M2L1\perros/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
