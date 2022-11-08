#! /usr/bin/python3

import discord, os, random, requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix="*", intents=discord.Intents.all())

class My_Cog(commands.Cog, name="deals"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='Slickdeals scraper' , brief='Gets deals from your query', description='Grabs deals from www.slickdeals.net and posts it to your current channel')
    async def test(ctx):
        await ctx.send('test')

@bot.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel)
    user_message = str(message.content)
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == bot.user:
        return
    
    if channel == "bot-testing":
        await bot.process_commands(message)
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'Bye {username}')

@bot.command()
async def options(ctx):
    if ctx == "*help":
        await ctx.send(f"""
            Usage: *help
            *h     : help page
         *deals      : slickdeals url
            """)
    elif ctx == "*deals":
        await ctx.send("www.slickdeals.net")

            

if __name__ == "__main__":
    bot.add_cog(My_Cog(bot))
    bot.run(token)
