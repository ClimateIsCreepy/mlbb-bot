import discord
from discord import message
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import context



class Layla(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def helpy(self,ctx):
        helpembed = discord.Embed(title="Help Commands For Layla", description="Here is the list of commands!", color=0x00ff00)
        helpembed.add_field(name="!help <tag>", value="Get specific information on a tag", inline=False)
        helpembed.add_field(name="!tags", value="Gets a list of tags", inline=False)
        await ctx.send(embed=helpembed)
    @commands.command()
    async def tags(self,ctx):
        tagsembed=discord.Embed(title="**List of tags**",description='``` do "!help <tag> to learn more about a specific tag" ```', color=0x00ff00)
        tagsembed.set_thumbnail(url='https://cdn.discordapp.com/attachments/882550997422067798/894812318771326986/layla.jpg')
        tagsembed.set_footer(text='**Need more help?**',icon_url='https://cdn.discordapp.com/attachments/882550997422067798/894812323657707580/layla2.png')
        tagsembed.add_field(name='**Utility tags**',value='``` ban, kick, mute, clear, serverstats, ping, avatar```',inline=False)
        await ctx.send(embed=tagsembed)
    
def setup(bot: commands.Bot):
    bot.add_cog(Layla(bot))
