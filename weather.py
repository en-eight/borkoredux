from discord.ext import commands

class Weather:
    """Weather forecast."""
    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context=True)
    async def weather(self):
        """
        IMPORTANT: Command disabled. For more info, bork weather.
        """
        await self.bot.say("As of January 3rd, 2018, Yahoo Weather has disabled its free API. " +
                                    "As frustrating and disappointing as this is, I am working tirelessly to find an alternative. "+
									"Thank you for your understanding.")

def setup(bot):
    bot.add_cog(Weather(bot))