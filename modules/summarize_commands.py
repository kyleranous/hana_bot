"""
MLA for summarizing text
"""

from discord.ext import commands
from handlers import summarize


class Summarize(commands.Cog):
    """
    Commands for summarizing text
    """

    @commands.command()
    async def summarize_url(self, ctx, url: str, per: float = 0.1):
        '''
        Takes in a URL and returns a summary of the artical found at the URL
        '''
        summary = summarize.summarize_url(url, per)
        msg = f'Here is the summary of {url}:\n{summary}'
        await ctx.reply(msg)