import discord #sa import le truc de discord
from discord.ext import commands #sa import discord 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), help_command=None, intents=intents)

if __name__ == '__main__':
    bot.run("YOUR_BOT_TOKEN")

