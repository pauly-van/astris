#! /usr/bin/python3

import discord, os, random, requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

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
        elif user_message.lower() == "deals":
            await message.channel.send("https://slickdeals.net/")

@bot.command()
async def options(ctx):
    if ctx == "$options -h" or "$options help":
        await ctx.send(f"""
            Usage: $help [option] 
            -h      : help page
         deals      : slickdeals url
            """)
            

if __name__ == "__main__":
    bot.run(token)
