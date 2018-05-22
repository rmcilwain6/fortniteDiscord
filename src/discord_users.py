#!/usr/bin/env python3

#opens up a discord client and grabs users from the server

import discord

TOKEN = 'NDQ4NTQ5MDgyNzc2OTkzODAz.DeXv0A.02Hqp8M2dUleupLlOeEa-SpdOqw'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    elif message.content.startswith('!members'):
        #get a list of all members in the server not including itself
        mem_list = message.server.members
        for member in mem_list:
            if member.name != 'scraper_bot':
                msg = member.name
                await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

def main():
    client.run(TOKEN)

if __name__ == "__main__":
    main()