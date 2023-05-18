"""
HANA Discord Chat Bot
"""

import os
import logging
import urllib.parse
import discord
from discord.ext import commands
import dotenv
from modules.github_commands import Github
from modules.math_commands import Math
from modules.summarize_commands import Summarize


dotenv.load_dotenv()

LOGGER = logging.getLogger(__name__)
# Setup LOGGER to print to the terminal
LOGGER.addHandler(logging.StreamHandler())

LOGGER.setLevel(logging.DEBUG)


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

DESCRIPTION = 'HANA Discord Bot'
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', description=DESCRIPTION, intents=intents)


@bot.event
async def on_ready():
    """ 
    Setup the bot when it is ready
    """
    print(f'We have logged in as {bot.user}')
    await bot.add_cog(Github(bot))
    await bot.add_cog(Math(bot))
    await bot.add_cog(Summarize(bot))


@bot.command()
async def url_encode(ctx, encode: str):
    """
    Recieves a string and returns the URL Encoded version
    EX: /url_encode "This is a string to encode"
    """
    LOGGER.debug('URL Encode request recieved: %s', encode)
    encoded_string = urllib.parse.quote(encode)
    await ctx.send(encoded_string)

bot.run(DISCORD_TOKEN)
