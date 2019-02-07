from discord.ext import commands
import pywikibot
PYWIKIBOT_NO_USER_CONFIG=1

class wikiScraper:
    """Wikipedia scraper."""
    def __init__(self, bot):
        self.bot=bot

    @commands.command(pass_context=True)
    async def wikiscraper(ctx, *, usersearch):
        site = pywikibot.Site()
        page = pywikibot.Page(site, u"{}".format(usersearch))
        text = page.text
        await self.bot.send_message("{}".format(text))


def setup(bot):
    bot.add_cog(wikiScraper(bot))