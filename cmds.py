import discord, json
from read import read
from slickdeals import scrapeSlickDeals
from stocks import scrapeYahooStock
from discord.ext import commands

class Main(commands.Cog):
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
    async def stock(self, ctx, arg):
        print(scrapeYahooStock(arg))
    #    await ctx.send("hi")
    #    await ctx.send_message(message.channel, f"The stock price for {stock.upper()} is ${stock_price} currently.")

    @commands.command(name='char-screen' , brief='List of family member screen name with real name association', description='List of family member screen name with real name association')
    async def test(self, ctx, func, name=None):
        members = read()
        peeps = "\n"
        match func:
            case "list":
                for key, value in members.items():
                    peeps += f"""Alias: `{key}`: Name: `{value}`\n"""
                await ctx.channel.send(peeps)
            case "add":
                pass
            case "delete":
                pass

def setup(bot):
    bot.add_cog(Main(bot))