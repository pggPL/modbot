import discord
from discord.ext import commands
from modbot.database.models import Mailbox
from modbot.database.mailbox_utils import get_mailboxes

class ShowMailboxes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def show_mailboxes(self, ctx: commands.Context):
        mailboxes = get_mailboxes(ctx.guild.id)

        result = ""

        for m in mailboxes:
            result += m.dc_show()

        await ctx.channel.send(result)



async def setup(bot):
    await bot.add_cog(ShowMailboxes(bot))
