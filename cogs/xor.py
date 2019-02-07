from discord.ext import commands
from itertools import cycle
import base64

class XOR:
    """XOR encryption. Key is BORKO."""

    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context=True)
    async def xor(self, ctx, *, userstring, decryptKey = 'BORKO'):
        """
        Uses XOR encryption to encrypt a string. Key is BORKO.
        """
        userXOR = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(userstring, cycle(decryptKey)))
        await self.bot.say ('**{}** is your encrypted string.'.format(userXOR))
def setup(bot):
    bot.add_cog(XOR(bot))