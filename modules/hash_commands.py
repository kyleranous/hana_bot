"""
Hash commands for HANA Bot
"""

import base64
from discord.ext import commands
from handlers import hash_generator


class Hash(commands.Cog):
    '''
    Hash Commands
    '''
    @commands.command()
    async def sha256(self, ctx, *args):
        '''
        Hashes a string using sha256
            EX: /sha256 hello world
        '''
        result = hash_generator.sha256_hash(' '.join(args))
        msg = f"The sha256 Hash of \'{' '.join(args)}\' is:\n{result}"
        await ctx.reply(msg)

    @commands.command()
    async def md5(self, ctx, *args):
        '''
        Hashes a string using md5
            EX: /md5 hello world
        '''
        result = hash_generator.md5_hash(' '.join(args))
        msg = f"The MD5 Hash of \'{' '.join(args)}\' is:\n{result}"
        await ctx.reply(msg)

    @commands.command()
    async def encode_b64(self, ctx, *args):
        '''
        Encodes a string in base64
            EX: /encode_b64 hello world
        '''
        result = base64.b64encode(bytes(' '.join(args), encoding='utf-8'), altchars=None)
        msg = f"The Base64 Encoded string of \'{' '.join(args)}\' is:\n{result.decode()}"
        await ctx.reply(msg)

    @commands.command()
    async def decode_b64(self, ctx, encode_string: str):
        '''
        Decodes a base64 string
            EX: /decode_b64 aGVsbG8gd29ybGQ=
        '''
        result = base64.b64decode(encode_string)
        msg = f"The decoded Base64 string of \'{encode_string}\' is:\n{result.decode()}"
        await ctx.reply(msg)
