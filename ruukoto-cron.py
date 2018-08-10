import asyncio
import discord
import os
import time
import traceback

client = discord.Client()

@client.event
async def on_ready():
    await client.send_message(client.get_channel('322184073420472334'), 'Testes da bot para mensagens automatizadas :thinking:')
    quit()   

client.run('MjM4NzQxMTMzNzc2MTI1OTUz.DJjuBg.mCVcxt6jGHdqRnfqmcvj_IJhtIo')
