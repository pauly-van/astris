import discord, json
from read import read
from read import update
from read import write
from commands.slickdeals import scrapeSlickDeals
from commands.stocks import getStock
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_member = None
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        chan = member.guild.system_channel
        if chan is not None:
            await chan.send(f"Welcome {member.mention}.")

    @commands.command() 
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

    @commands.command(name='deals' , brief='Gets deals from your query or top page items', description='Grabs deals from www.slickdeals.net and posts it to your current channel')
    async def deals(self, ctx, arg=10):
        deals = scrapeSlickDeals()
        items = int(arg)
        for d in range(items):
            await ctx.channel.send(
                f"""
                {deals[d]["title"]} 
                {deals[d]["link"]}
                {deals[d]["price"]} 
                """)

    @commands.command(name='stocks', brief='Get stock prices of added ticker or popular lists', description='Post to channel stock prices of arbitrary tickers or list top from site')
    async def stock(self, ctx, arg, func=None):
        match func:
            case None:
                stock = getStock(arg)
                await ctx.channel.send(f"""
                                {stock['longName']}
                                {stock['currentPrice']}
                                {stock['logo_url']}
                                """)
            case 'list':
                pass
            case 'add':
                pass
            case 'delete':
                pass

    @commands.command(name='characters' , brief='List of family member screen name with real name association', description='List of family member screen name with real name association')
    async def characters(self, ctx, func, alias=None, name=None):
        members = read()
        match func:
            case "list":
                peeps = ""
                for key, value in members.items():
                    peeps += f"""Alias: `{key}`: Name: `{value}`\n"""
                await ctx.channel.send(peeps)
            case "add":
                update(func, alias, name)
            case "delete":
                update(func, alias, name)
            case "update":
                pass

def setup(bot):
    bot.add_cog(Commands(bot))