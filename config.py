import discord
import os
client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '#'
commands = ['commands', 'play']
activity = discord.Activity(
    type=discord.ActivityType.listening, name="!commands")
