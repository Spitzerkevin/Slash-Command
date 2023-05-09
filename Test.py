import os
import discord
from discord.ext import commands


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.tree.command(name = "test", description="This is a test")
async def test(interaction: discord.Interaction):

 await interaction.response.send_message("Test")


@bot.event
async def on_ready():
  print("Bot Is Ready")
  try:        
    await bot.tree.sync()
  except Exception as e:
    print(e)


bot.run(os.environ['token'])