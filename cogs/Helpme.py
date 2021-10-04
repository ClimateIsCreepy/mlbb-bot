import os
import discord
from discord import message
from discord import channel
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context


class Helpme(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def helps(self,ctx):
        helpembed = discord.Embed(title="Help Commands For Layla", description="Here is the list of commands!", color=0x00ff00)
        helpembed.add_field(name="!help <tag>", value="Get specific information on a tag", inline=False)
        helpembed.add_field(name="!tags", value="Gets a list of tags", inline=False)
        await ctx.send(embed=helpembed)
def setup(bot: commands.Bot):
    bot.add_cog(Helpme(bot))
