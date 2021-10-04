import os
from typing import List
import discord
from discord import message
from discord.errors import ClientException
from discord.ext import commands
import DiscordUtils
from discord import Member
import random
from discord.ext.commands import context
from discord.ext import commands
from discord.ext.commands.core import command 

class SomeCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.command()
    async def bruh(self,ctx):
        await ctx.send("bruh")
    @commands.Cog.listener() # this is a decorator for events/listeners
    async def on_ready(self):
      print('Bot is ready!.')
def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))
