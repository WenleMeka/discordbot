# bot.py
import discord

import os
import asyncio
import datetime
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Client = commands.Bot(command_prefix='w!')

def status(Client):
    @Client.event
    async def on_ready():
        await client.change_preence(status=discord.Status.idle, activity=discord.Game('Trabajando', 'Para más ayuda **w!help**' ))
    
    Client.run(TOKEN)