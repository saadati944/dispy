import discord
import asyncio
import config
import data
from discord.ext import commands

members=[]
client = discord.Client()

@client.event
async def on_ready():
    global members
    for guild in client.guilds:
        if guild.name==config.guild:
            pass#break
        print(f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})\n')
    members = [member.name for member in guild.members]
    print('Guild Members:\n - '+'\n - '.join(members))
    #await guild.members[0].create_dm()
    #await guild.members[0].dm_channel.send(f'Hi {guild.members[0]}, welcome to my Discord server!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')
    await member.dm_channel.send(data.get_static_data('welcome'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content[0]=='$' and not ' ' in message.content:
        await message.channel.send(data.get_static_data(message.content[1:]))
        return
    response = 'hello '+message.author.name+'\n you have sent : '+message.content
    await message.channel.send(response)
    await message.channel.send(file=discord.File(config.image0))



client.run(config.token)
