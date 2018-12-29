import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '$')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    await client.change_presence(game=Game(name='Sayur Kol Simulator'))
    await client.send_message(member, 'WELCOME TO FRIENDS! SEKARANG YOU ARE OUR FRIENDS.')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$owner':
        await client.send_message(message.channel,'KUBUS#1749 dan NADYA KENTANG#5975')
    if message.content == '$botmaker':
        await client.send_message(message.channel,'potatos.#0707')
    if message.content == '$vape':
        await client.send_message(message.channel,'ngevape kok onlen boedjank')
    if message.content == '$rules':
        await client.send_message(message.channel,'baca #rules-✉ saja bang :3')
    if message.content.startswith('Halo'):
        await client.send_message(message.channel,'Halo Juga <@%s> :D'  %(message.author.id))
    if message.content == '$invitelink':
        await client.send_message(message.channel,'https://discord.gg/Ay3nW7s')
    if message.content.startswith('$gw ganteng?'):
        randomlist = ["iya","tidak",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if ('kontol') in message.content:
       await client.delete_message(message)
    if ('anjing') in message.content:
       await client.delete_message(message)
    if ('memek') in message.content:
       await client.delete_message(message)
    if ('bangsad') in message.content:
       await client.delete_message(message)
    if ('bangsat') in message.content:
       await client.delete_message(message)
    if message.content == 'kontol':
        await client.send_message(message.channel,'tolong mulutnya dijaga ya :D')
    if message.content == 'bangsat':
        await client.send_message(message.channel,'tolong mulutnya dijaga ya :D')
    if message.content == 'bangsad':
        await client.send_message(message.channel,'tolong mulutnya dijaga ya :D')
    if message.content == 'tolol':
        await client.send_message(message.channel,'tolong mulutnya dijaga ya :D')
    if ('tolol') in message.content:
       await client.delete_message(message)
    if message.content == 'goblok':
        await client.send_message(message.channel,'mulutnya dijaga ya :D')
    if message.content.startswith('$gw cantik?'):
        randomlist = ["iya","tidak",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '$banana':
        em = discord.Embed(description='hayu joged yu.')
        em.set_image(url='https://imgur.com/a/fsM24e7')
        await client.send_message(message.channel, embed=em)
client.run('NTI4MTc2NTc4ODkxNjEyMTYw.DwefAA.0k_wPuyfmD7pJMtHeOq9cdy3hEs')


   






client.run(str(os.environ.get('BOT_TOKEN')))
