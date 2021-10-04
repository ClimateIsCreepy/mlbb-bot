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
from discord.ext.commands.bot import Bot 
 
bot = commands.Bot(command_prefix='!')

bot.load_extension(
    "cogs.Helpme"
)
bot.load_extension(
    "cogs.SomeCommands"
)
bot.run("ODk0NDMzMjA3NTQ0NTgyMTU0.YVp71g.1Td_V5vHLGWAqa3FxTldLJ1zBnM")
