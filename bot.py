from discord.ext import commands

 
bot = commands.Bot(command_prefix='!')

bot.load_extension(
    "cogs.Helpme"
)
bot.load_extension(
    "cogs.SomeCommands"
)
bot.run("TOKEN")
