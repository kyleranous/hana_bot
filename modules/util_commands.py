"""
Utility Class for performing various functions with HANA Bot
"""
import logging
import urllib.parse
import requests
import discord
from discord.ext import commands
from handlers import qr_generator


LOGGER = logging.getLogger('discord')
LOGGER.setLevel(logging.DEBUG)

class Utils(commands.Cog):
    """
    Commands for General Utility functions
    """

    @commands.command()
    async def create_qr(self, ctx, data: str):
        '''
        Take in a string, generate a QR Code and send it to the user
        '''
        LOGGER.info('Create QR request recieved: %s From User %s', data, ctx.author.name)
        img_path = qr_generator.generate_qr_code(data)
        await ctx.reply(file=discord.File(img_path))

    @commands.command()
    async def define(self, ctx, word: str):
        '''
        Take in a word and return the definition
        '''
        LOGGER.info('Define request recieved: %s From User %s', word, ctx.author.name)
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
            LOGGER.warning('Error fetching definition: %s', response.text)
            msg = f"Unable to find a definition for {word}. "
            msg += "Please try again in a little bit or let Kyle know."
            await ctx.reply(msg)

    @commands.command()
    async def url_encode(self, ctx, encode: str):
        """
        Recieves a string and returns the URL Encoded version
        EX: /url_encode "This is a string to encode"
        """
        LOGGER.debug('URL Encode request recieved: %s', encode)
        encoded_string = urllib.parse.quote(encode)
        await ctx.reply(encoded_string)
