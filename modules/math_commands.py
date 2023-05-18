"""
Math commands for HANA Bot
"""

from discord.ext import commands


class Math(commands.Cog):
    """
    Math commands
    """
    @commands.command()
    async def add(self, ctx, *args):
        '''Adds numbers together. Must have at least 2 numbers
            EX /add 1 2 3 4 5
        '''
    #LOGGER.debug('Add request recieved: %s', args)
        if len(args) < 2:
            await ctx.reply('You must provide at least 2 numbers to add')
            return
    
        total = 0.0
        for arg in args:
            total += float(arg)

        await ctx.reply(total)
