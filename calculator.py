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

def calculator(Client):
    @Client.command(name='sumar')
    async def sum(ctx, numOne: int, numTwo: int):
        operation = numOne + numTwo
        await ctx.send(f'El resultado de la suma eeees redoble de tamboreeeees tum tum: {operation}')


    @Client.command(name='multiplicar')
    async def mult(ctx, numOne: int, numTwo: int):
        operation = numOne * numTwo
        await ctx.send(f'El resultado de la multiplicación eeees redoble de tamboreeeees tum tum: {operation}')


    @Client.command(name='dividir')
    async def divi(ctx, numOne: int, numTwo: int):
        operation = numOne / numTwo
        await ctx.send(f'El resultado de la división eeees redoble de tamboreeeees tum tum: {operation}')


    @Client.command(name='restar')
    async def rest(ctx, numOne: int, numTwo: int):
        operation = numOne - numTwo
        await ctx.send (f'El resultado de la resta eeees redoble de tamboreeeees tum tum: {operation}')


    @Client.command(name='modulo')
    async def módu(ctx, numOne: int, numTwo: int):
        operation = numOne % numTwo
        await ctx.send (f'El resultado del módulo eeees redoble de tamboreeeees tum tum: {operation}')


    @Client.command(name='exponenciacion')
    async def expo(ctx, numOne: int, numTwo: int):
        operation = numOne ** numTwo
        await ctx.send (f'El resultado del exponenciación eeees redoble de tamboreeeees tum tum: {operation}')

    Client.run(TOKEN)
