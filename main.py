#/home/sagira/bin/python3.5
import discord
import configparser
import asyncio

discordconf = configparser.ConfigParser()
discordconf.read('discord-token.ini')

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		msg = 'Hello Osiris'.format(message)
		await client.send_message(message.channel, msg)
	
	if message.content.lower().startswith('ayy'): 
		msg = 'lmao'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.lower().startswith('!triggered'):
		msg = 'https://i.imgur.com/S9k1k9U.gif'.format(message)
		await client.send_message(message.channel, msg)

	if message.content.lower().startswith('!mars'):
		msg = "```Whether we wanted it or not, we've stepped into a war with the Cabal on Mars. So let's get to taking out their command, one by one. Valus Ta'aurc. From what I can gather he commands the Siege Dancers from an Imperial Land Tank outside of Rubicon. He's well protected, but with the right team, we can punch through those defenses, take this beast out, and break their grip on Freehold.```"
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-------')

client.run(discordconf['discord']['token'])
