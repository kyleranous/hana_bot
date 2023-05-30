"""
Math commands for HANA Bot
"""
import math
from discord.ext import commands


class Math(commands.Cog):
    """
    Math commands
    """
    @commands.command()
    async def sum(self, ctx, *args):
        '''
        Adds numbers together. Must have at least 2 numbers
            EX /add 1 2 3 4 5
        '''
    #LOGGER.debug('Add request recieved: %s', args)
        if len(args) < 2:
            await ctx.reply('You must provide at least 2 numbers to add')
            return

        total = math.fsum([float(arg) for arg in args])

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

    @commands.command()
    async def sqrt(self, ctx, num):
        '''
        Returns the square root of a number
            EX /sqrt 4
        '''
        await ctx.reply(float(num) ** 0.5)

    @commands.command()
    async def log(self, ctx, num, base=math.e):
        '''
        Returns the log of a number. If no base is specified, will return the natural log
            EX /log 10
            EX /log 10 2
        '''
        await ctx.reply(math.log(float(num), base))

    @commands.command()
    async def mean(self, ctx, *args):
        '''
        Returns the mean of a list of numbers
            EX /mean 1 2 3 4 5
        '''
        total = 0.0
        for arg in args:
            total += float(arg)

        await ctx.reply(total / len(args))

    @commands.command()
    async def median(self, ctx, *args):
        '''
        Returns the median of a list of numbers
            EX /median 1 2 3 4 5
        '''
        args = sorted(args)
        if len(args) % 2 == 0:
            await ctx.reply((float(args[len(args) // 2]) + float(args[(len(args) // 2) - 1])) / 2)
        else:
            await ctx.reply(args[len(args) // 2])

    @commands.command()
    async def mode(self, ctx, *args):
        '''
        Returns the mode of a list of numbers
            EX /mode 1 2 3 4 5
        '''
        mode = None
        mode_count = 0
        for arg in args:
            if args.count(arg) > mode_count:
                mode = arg
                mode_count = args.count(arg)
        await ctx.reply(mode)

    @commands.command()
    async def order(self, ctx, *args):
        '''
        Returns a list of numbers in order
            EX /order 5 2 3 1 4
        '''
        await ctx.reply(sorted(args))

    @commands.command()
    async def factorial(self, ctx, num):
        '''
        Returns the factorial of a number
            EX /factorial 5
        '''
        await ctx.reply(math.factorial(int(num)))

    @commands.command()
    async def sin(self, ctx, num):
        '''
        Returns the sine of a number
            EX /sin 90
        '''
        await ctx.reply(math.sin(math.radians(float(num))))

    @commands.command()
    async def cos(self, ctx, num):
        '''
        Returns the cosine of a number
            EX /cos 90
        '''
        await ctx.reply(math.cos(math.radians(float(num))))

    @commands.command()
    async def tan(self, ctx, num):
        '''
        Returns the tangent of a number
            EX /tan 90
        '''
        await ctx.reply(math.tan(math.radians(float(num))))

    @commands.command()
    async def asin(self, ctx, num):
        '''
        Returns the arcsine of a number
            EX /asin 1
        '''
        await ctx.reply(math.degrees(math.asin(float(num))))

    @commands.command()
    async def acos(self, ctx, num):
        '''
        Returns the arccosine of a number
            EX /acos 1
        '''
        await ctx.reply(math.degrees(math.acos(float(num))))

    @commands.command()
    async def atan(self, ctx, num):
        '''
        Returns the arctangent of a number
            EX /atan 1
        '''
        await ctx.reply(math.degrees(math.atan(float(num))))

    @commands.command()
    async def sinh(self, ctx, num):
        '''
        Returns the hyperbolic sine of a number
            EX /sinh 1
        '''
        await ctx.reply(math.sinh(float(num)))

    @commands.command()
    async def cosh(self, ctx, num):
        '''
        Returns the hyperbolic cosine of a number
            EX /cosh 1
        '''
        await ctx.reply(math.cosh(float(num)))

    @commands.command()
    async def tanh(self, ctx, num):
        '''
        Returns the hyperbolic tangent of a number
            EX /tanh 1
        '''
        await ctx.reply(math.tanh(float(num)))

    @commands.command()
    async def asinh(self, ctx, num):
        '''
        Returns the inverse hyperbolic sine of a number
            EX /asinh 1
        '''
        await ctx.reply(math.asinh(float(num)))

    @commands.command()
    async def acosh(self, ctx, num):
        '''
        Returns the inverse hyperbolic cosine of a number
            EX /acosh 1
        '''
        await ctx.reply(math.acosh(float(num)))

    @commands.command()
    async def atanh(self, ctx, num):
        '''
        Returns the inverse hyperbolic tangent of a number
            EX /atanh 1
        '''
        await ctx.reply(math.atanh(float(num)))
