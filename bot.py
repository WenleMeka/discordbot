# bot.py
import discord

import os
import asyncio
import datetime
import random
from discord.ext import commands
from dotenv import load_dotenv
import calculator, moderation, statuss, info

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Client = commands.Bot(command_prefix='w!')

calculator.calculator(Client)
moderation.moderation(Client)
statuss.status(Client)
info.info(Client)
