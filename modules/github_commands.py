"""
Commands for interacting with GitHub
"""
from discord.ext import commands


class Github(commands.Cog):
    """
    Commands HANA uses to interact with GitHub
    """
    @commands.command()
    async def create_issue(self, ctx, title, body):
        """
        Creates a Github Issue
        EX: /create_issue "This is the Title" "This is the Body"
        """

        await ctx.send(f"Creating a new Issue: {title}\n{body}")
