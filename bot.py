# bot.py
import os

import datetime

import random

from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='w!')

@bot.command(name='wenle')
async def prueba(ctx):
    respuesta_bot = 'Hey, soy un bot y estoy haciendo pruebas. Bitbot bitbitbot'

    await ctx.send(respuesta_bot)
    
@bot.command(name='hola')
async def hola(ctx):
    respuesta_bot = 'hola, que tal estas?'
    
    await ctx.send(respuesta_bot)

@bot.command(name='bien')
async def contestar(ctx):
    respuesta_bot = 'estoy muy bien, gracias!'

    await ctx.send(respuesta_bot)

@bot.command(name='sumar')
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command(name='info')
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Este es el server de WenleMeka", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://img.favpng.com/2/11/12/weather-forecasting-rain-icon-png-favpng-YgZVGY0BZc3miKJQa4m8EicHb.jpg")

    await ctx.send(embed=embed)


bot.run(TOKEN)