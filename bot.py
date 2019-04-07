import discord
import asyncio

description = "Baylor-Bot"
bot_prefix = "!"

client = discord.Client()

@client.event
async def on_ready():
	print("Logged in");
	print("Name: " + client.user.name);
	print("ID: " + client.user.id);
	print("\n\n");

@client.event
async def on_message(message):
	if message.content.startswith('!help'):
		await client.send_message(message.channel, "HELP")

client.run("-- REDACTED --"); 
