import os
import discord
from discord import message
from discord.ext.commands import context
client = discord.Client()
class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.command()
    async def help(self,ctx):
        helpembed = discord.Embed(title="Help Commands For Layla", description="Here is the list of commands!", color=0x00ff00)
        helpembed.add_field(name="!help <tag>", value="Get specific information on a tag", inline=False)
        helpembed.add_field(name="!tags", value="Gets a list of tags", inline=False)
        await ctx.send("helpembed")
def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
