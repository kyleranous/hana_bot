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
        '''
        Adds numbers together. Must have at least 2 numbers
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

    @commands.command()
    async def mult(self, ctx, *args):
        '''
        Multiplies numbers together. Must have at least 2 numbers
            EX /mult 1 2 3 4 5
        '''
        if len(args) < 2:
            await ctx.reply('You must provide at least 2 numbers to multiply')
            return

        total = 1
        for arg in args:
            total *= float(arg)

        await ctx.reply(total)

    @commands.command()
    async def  div(self, ctx, dividend, divisor):
        '''
        Divides two numbers
            EX /div 10 2
        '''
        if divisor == 0:
            await ctx.reply('You cannot divide by zero')
            return

        await ctx.reply(float(dividend) / float(divisor))

    @commands.command()
    async def exp(self, ctx, base, exp):
        '''
        Raises a number to a power. for
            EX: For 2^3 use /exp 2 3
        '''
        await ctx.reply(float(base) ** float(exp))
