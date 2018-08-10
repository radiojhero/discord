import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import xml.etree.cElementTree as et
import xml.dom.minidom
from xml.dom.minidom import Node

client = discord.Client()
channel = discord.Object(id='322175431061012481')


@client.event
async def on_ready():
    channel = '322175431061012481'
    print("Ruu... Ruu... Ruu...")
    print("Ruukoto serve {}".format(client.user.name))
    print("ID {}".format(client.user.id))

@client.event
async def on_message(message):
    await client.send_message(message.channel, 'Teste da Ruukoto para Anúncios')
    exit()

  

client.run("MjM4NzQxMTMzNzc2MTI1OTUz.DJjuBg.mCVcxt6jGHdqRnfqmcvj_IJhtIo")
