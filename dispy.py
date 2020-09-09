import discord
import asyncio
import config
import data
from discord.ext import commands
import os

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
    #return if message is from bot it self
    if message.author == client.user:
        return
    #static messages
    if message.content[0]=='$' and not ' ' in message.content:
        await sendStaticMessages(message.channel,message.content[1:],True)
        return
    if message.content=='test':
        res='test message'
        await message.channel.send(res, embed=imageembed(config.image0))
        return
    
    '''
    response = 'hello '+message.author.name+'\n you have sent : '+message.content
    await message.channel.send(response)
    await message.channel.send(file=discord.File(config.image0))
    '''

#ch is discord.Channel
#name is the name of static message file
async def sendStaticMessages(ch,name,user=False):
    mescontent=data.get_static_data(name,user)
    #don't send anything if message content is empty.
    if len(mescontent)==0:
        return
    #if message content starts with a ! , don't apply formatting.
    if mescontent[0][0]=='!':
        mescontent[0]=mescontent[0][1:]
        await ch.send(''.join(mescontent))
        return
    #don't apply formatting if lines are fewer than 6
    if len(mescontent)<6:
        await ch.send(''.join(mescontent))
        return
    imglink=''
    nextmes=''
    #first 5 lines are reserved for formatting.
    for i in range(5):
        l0=mescontent.pop(0)
        if l0[-1]=='\n':
            l0=l0[:-1]
        if l0.startswith('image:'):
            imglink=l0[6:]
        elif l0.startswith('next:'):
            nextmes=l0[5:]
    if imglink=='':
        await ch.send('\n'.join(mescontent))
    elif os.path.exists(imglink):
        await ch.send('\n'.join(mescontent),file=file(imglink))
    else:
        await ch.send('\n'.join(mescontent),embed=imageembed(imglink))
    if not nextmes=='':
        await sendStaticMessages(ch,nextmes)


#files and mentions
def file(pth):
    return discord.File(pth)
def imageembed(url):
    return discord.Embed().set_image(url=url)

#formating functions :
def bold(mes):
    return '**'+mes+'**'
def italic(mes):
    return '*'+mes+'*'
def underline(mes):
    return '__'+mes+'__'
def strike(mes):
    return '~~'+mes+'~~'
def code(mes):
    if '\n' in mes:
        return ' `'+mes+'` '
    return ' ```'+mes+'``` '
def quote(mes):
    mes.replace('\n','\n> ')
    return '> '+mes


client.run(config.token)
