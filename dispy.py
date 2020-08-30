import discord
import asyncio
import config
from discord.ext import commands


client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name==config.guild:
            pass#break
        print(f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    #await guild.members[0].create_dm()
    #await guild.members[0].dm_channel.send(f'Hi {guild.members[0]}, welcome to my Discord server!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else :
        response = 'hello '+message.author.name+'\n you have sent : '+message.content
        await message.channel.send(response)

client.run(config.token)
