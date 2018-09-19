#/home/sagira/bin/python3.5
import discord
import configparser
import asyncio
import requests
from urllib.request import quote

discordconf = configparser.ConfigParser()
discordconf.read('discord-token.ini')

client = discord.Client()

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	#basic message responses
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

	if message.content.lower().startswith('!badbot'):
		msg = "You're not even my real guardian."
		await client.send_message(message.channel, msg)

	#messing around with role assigning
	if message.content.startswith("!setrole"):
		console_list = ["Playstation", "Xbox", "PC"] #available roles
		entered_console = message.content[9:] #counting characters from your command to the console entries, IE 9 for "!setrole " including the space
		role = discord.utils.get(message.server.roles, name=entered_console) #retrieve existing roles
		roles = [
			"314858732204851210", #Playstation
			"314859151152906243", #Xbox
			"352277227951489024", #PC
		]
		for r in message.author.roles:
			if r.id in roles:
				#yell at them if they already have a role
				await client.send_message(message.channel, "You already have a role Guardian, maybe you need to go get yelled at by Zavala")
				return
		if role is None or role.name not in console_list:
			#Complain if the role doesn't exist
			await client.send_message(message.channel, "That console doesn't exist Guardian. Please use Playstation Xbox or PC")
			return
		elif role in message.author.roles:
			#if they're already got it
			await client.send_message(message.channel, "You already have this console, Guardian.")
		else:
			try:
				await client.add_roles(message.author, role)
				await client.send_message(message.channel, "Successfully added role {0}".format(role.name))
			except discord.Forbidden:
				await client.send_message(message.channel, "I don't have perms to add roles") #either bot doesn't have the "Manage roles" permission, or it's below the needed roles in the priority list

	# Retrieving lore entries from ishtar
	if message.content.startswith("!lore"):
		search_term = quote(message.content[6:]) # Site is bad so we have to URL-encode these
		entries_term = (message.content[6:].replace(' ', '-')) # and convert spaces to - for these
		entries_url = ("https://www.ishtar-collective.net/entries/" + entries_term)
		search_url = ("https://www.ishtar-collective.net/search/" + search_term)
		r = requests.get(entries_url)
		if r.status_code == requests.codes.ok:
			msg = (entries_url)
			await client.send_message(message.channel, msg)
		else:
			msg = (search_url)
			await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-------')

client.run(discordconf['discord']['token'])
