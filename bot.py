import discord
import asyncio
import json

def read_config():
	with open("config.json") as configFile:
		return json.load(configFile)
	
config = read_config()

description = config["description"]
bot_prefix = config["prefix"]

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

try:
	client.run(config["token"])
except Exception as e:
	print("Error connecting to Discord: "+e)
