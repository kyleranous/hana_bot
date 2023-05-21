"""
MLA for summarizing text
"""
import logging
from discord.ext import commands
from handlers import summarize

LOGGER = logging.getLogger('discord')
# Setup LOGGER to print to the terminal
# LOGGER.addHandler(logging.StreamHandler())

#LOGGER.setLevel(logging.DEBUG)
class Summarize(commands.Cog):
    """
    Commands for summarizing text
    """

    # Define Parameters
    percentage = commands.parameter(description="Percentage of original text in summary",
                                    default=0.1)
    article_url = commands.parameter(description="URL to Article")

    @commands.command()
    async def summarize_url(self, ctx,
                            url: str=article_url,
                            per: float=percentage):
        '''
        Takes in a URL and returns a summary of the artical found at the URL
        '''
        LOGGER.info('Summarize URL request recieved: %s From User %s', url, ctx.author.name)
        summary = summarize.summarize_url(url, per)
        msg = f'Here is the summary of {url}:\n{summary}'
        await ctx.reply(msg)
