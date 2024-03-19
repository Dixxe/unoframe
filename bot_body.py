import disnake as ds
from disnake.ext import commands

# Defining token from file. 
token = str
with open("token.txt", "r") as f:
    token = f.read()

client = ds.Client()

intents = ds.Intents.default()
intents.message_content = True

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.Bot(command_prefix=">", 
                   intents=intents, 
                   command_sync_flags=command_sync_flags
                  )

@client.event
async def on_ready():
    print(f"Logged to {client.user}")

@bot.slash_command(description="Respond")
async def hello(inter):
    await inter.response.send_message("world")

client.run(token)