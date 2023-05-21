"""
HANA Discord Chat Bot
"""

import os
import logging

import discord
from discord.ext import commands
import dotenv
from modules.github_commands import Github
from modules.math_commands import Math
from modules.summarize_commands import Summarize
from modules.util_commands import Utils


dotenv.load_dotenv()


LOGGER = logging.getLogger('discord')
# Setup LOGGER to print to the terminal
#LOGGER.addHandler(logging.StreamHandler())

LOGGER.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)


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
    LOGGER.info('Logged in as %s', bot.user)
    await bot.add_cog(Github(bot))
    await bot.add_cog(Math(bot))
    await bot.add_cog(Summarize(bot))
    await bot.add_cog(Utils(bot))


bot.run(DISCORD_TOKEN)
