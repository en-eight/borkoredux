#Borko Redux
#code by n8#7612
#====================================================================================================================
from discord.ext.commands import Bot, errors
from discord.ext import commands
import sys, traceback, discord
#====================================================================================================================
PYWIKIBOT_NO_USER_CONFIG=1
token = open("token.txt", 'r')
Client = discord.Client()
startup_extensions = ["cogs.xor", "cogs.weather", "cogs.hello"]
#====================================================================================================================
bot = Bot(description='Borko Redux by n8#7612 :>', command_prefix='bork ', pm_help = False)

if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Unable to load extension {}'.format(extension), file = sys.stderr)
            traceback.print_exc()
#====================================================================================================================
@bot.event
async def on_command_error(error, ctx):
    """this is called when a command throws an error"""
    if isinstance(error, errors.NoPrivateMessage):
        await bot.send_message(ctx.message.channel, "The command you want to use cannot be used in DMs.")

    elif isinstance(error, errors.CommandOnCooldown):
        await bot.send_message(ctx.message.channel, "The command you want to use is currently cooling down. Try again in" 
                                                     "**{}** seconds.".format(error.retry_after))
    elif isinstance(error, errors.DisabledCommand):
        await bot.send_message(ctx.message.channel, "The command you want to use is disabled, meaning it can't be used. Sorry!")

    elif isinstance(error, errors.CommandNotFound):
            await bot.send_message(ctx.message.channel, "{} didn't match any of my commands. Use ``bork help`` for a list of commands.".format(ctx.message.content))
#====================================================================================================================
@bot.event
async def on_ready():
    print("I'm logged in as {}!".format(bot.user.name))
    print("Client ID is: {}!".format(bot.user.id))
    await bot.change_presence(game = discord.Game(name = "Super Mario Bros. 2 GOTY"))
    print("Successfully logged in! :>")

bot.run(token.read(), bot = True, reconnect = True)
#====================================================================================================================