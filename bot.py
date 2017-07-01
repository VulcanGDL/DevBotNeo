import discord
from discord.ext import commands
import time
import inspect
import random

description = '''idk what to put here'''
bot = commands.Bot(command_prefix='//', description='Dev bot Neo is what we test before putting into Dev Bot. Developed by Vulcan and Codfish246')
#ext_commands = ["moderation","developers","general"] #see line 24 ¦ we arent using exts in neo **yet**

@bot.event
async def on_ready():
    print('------------------------------------')
    print('Logged in successfully!')
    print('Name : {}'.format(bot.user.name))
    print('Bot ID : {}'.format(bot.user.id))
    print('Invite me using this invite link: https://discordapp.com/oauth2/authorize?client_id=330663866851786753&scope=bot&permissions=469765175')
    print('------------------------------------')
    print('Discord.py Wersion:')
    print(discord.__version__) #discord.py version
    print('------------------------------------')
    await bot.change_presence(game=(discord.Game(name="Dev Bot Neo!"))) #Bots game status
#    for i in range(len(ext_commands)+1): #line 9

    #    bot.load_extension(ext_commands[i-1]) #should load in other files from external commands but it doesnt ¦ line 9

@bot.command(name='ping')
async def ping():
    """Ping Command"""
    await bot.say(':ping_pong: Pong!')



bot.run('token')
