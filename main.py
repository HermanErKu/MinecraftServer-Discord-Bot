#HermanErKu 2021
#https://github.com/HermanErKu

import discord
import os
import time

Client = discord.Client()

#Your discord bot token  discord.com/developers
TOKEN = "1234"


#When bot is started
@Client.event
async def on_ready():
    print("{0.user}".format(Client))


#When bot recieves messages
@Client.event
async def on_message(message):
    if message.author == Client.user:
        return

    msg = message.content

    #command for starting server
    if msg.startswith("!startserver"):
        await message.channel.send("starting minecraft server")
        await message.channel.send("this takes about 10-20 seconds")
        os.system(r"test.bat") #your start.bat file for minecraft server (readme.md)
        await message.channel.send("server is started")

    #command for testing if the bot is working
    if msg.startswith("!test"): 
        await message.channel.send("I am working")
        await message.channel.send("thank you for asking")


#Your token so the bot can run
Client.run(TOKEN)