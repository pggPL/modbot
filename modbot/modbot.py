import sqlite3
import discord
from discord.ext import commands

# import modbot.database as database
# from modbot.commands import first_message, reset_configuration


class ModBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        # self.db_conn = sqlite3.connect('mybot.db')
        # database.init()
        
    async def on_guild_join(self, guild):
        print(f'Dołączono do nowej gildii: {guild.name}')
        # create channel and send message
        channel = await guild.create_text_channel('mybot')
        await channel.send('Witaj na serwerze!')
    
    # async def on_ready(self):
    #     print(f'Zalogowano jako {self.user}')
    #     for g in self.guilds:
    #         await first_message(g)

bot = ModBot(command_prefix='/', intents=discord.Intents.all())
# @bot.command(name='reset')
# async def reset_cmd(ctx):
#     await reset_configuration(ctx)

