"""
Utility Class for performing various functions with HANA Bot
"""
import requests
import discord
from discord.ext import commands
from handlers import qr_generator


class Utils(commands.Cog):
    """
    Commands for General Utility functions
    """

    @commands.command()
    async def create_qr(self, ctx, data: str):
        '''
        Take in a string, generate a QR Code and send it to the user
        '''
        img_path = qr_generator.generate_qr_code(data)
        await ctx.reply(file=discord.File(img_path))

    @commands.command()
    async def define(self, ctx, word: str):
        '''
        Take in a word and return the definition
        '''
        url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'

        response = requests.request("GET", url, timeout=10)

        if response.status_code == 200:
            msg = f"Definitions for {word}:\n"
            for meaning in response.json()[0]['meanings']:
                msg += f"{meaning['partOfSpeech']}:\n"
                for definition in meaning['definitions']:
                    msg += f"{definition['definition']}\n"

            await ctx.reply(msg)

        else:
            msg = f"Unable to find a definition for {word}."
            msg += "Please try again in a little bit or let Kyle know."
            await ctx.reply(msg)
