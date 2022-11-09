#! /usr/bin/python3

import discord, os, random, requests
from dotenv import load_dotenv
from discord.ext import commands
from slickdeals import scrapeSlickDeals

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())

class My_Cog(commands.Cog, name="deals"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Slickdeals scraper' , brief='Gets deals from your query', description='Grabs deals from www.slickdeals.net and posts it to your current channel')
    async def test(ctx):
        await ctx.send("hi")
            

@bot.command(name="deals")
async def deals(ctx):
    deals = scrapeSlickDeals()
    for d in range(5):
        await ctx.channel.send(
            f"""
            {deals[d]["title"]} 
            {deals[d]["link"]}
            {deals[d]["price"]} 
            """)


@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel)
    user_message = str(message.content)
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == bot.user:
        return
    
    if channel == "bot-testing" or "town-square":
        await bot.process_commands(message)
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')


if __name__ == "__main__":
    bot.add_cog(My_Cog(bot))
    bot.run(token)
