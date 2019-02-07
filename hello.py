from discord.ext import commands
import random

class Greetings:
	BORK_GREETINGS = ["Hello.", "Hey.", "What's up, mang?", "Yo yo yo, what's good in the hood?"]

class Hello:
    """Say hello."""
    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context = True)
    async def hello(self):
        """Say hello."""
        await self.bot.say('{}'.format(random(BORK_GREETINGS)

def setup(bot):
    bot.add_cog(Hello(bot))