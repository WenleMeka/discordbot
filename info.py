# bot.py
import discord
import os
import asyncio
import datetime
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Client = commands.Bot(command_prefix='w!')

def info(Client):
    @Client.command(name='info')
    async def info(ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description="Server Info", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        # embed.set_thumbnail(url=f"{ctx.guild.icon}")
        embed.set_thumbnail(url="https://mk0droplrg5q83m5xg0r.kinstacdn.com/wp-content/uploads/2020/06/iconfinder_discord_2308078-512x400.png")

        await ctx.send(embed=embed)
    
    Client.run(TOKEN)