import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("bot ready")


bot.load_extension(
    "cogs.Layla"
)
bot.load_extension(
    "cogs.SomeCommands"
)

bot.run("ODk0NDMzMjA3NTQ0NTgyMTU0.YVp71g.fxFfhzMbd88vAMU8j8xhgXRoHl8")
