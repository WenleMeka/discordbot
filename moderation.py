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

bot = discord.Client()

def moderation(Client):
    @Client.command(name='clear1')
    async def clear(ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    @Client.command(name='kick')
    async def kick(ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @Client.command(name='ban')
    async def ban(ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @Client.command(name='unban')
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return
    Client.run(TOKEN)