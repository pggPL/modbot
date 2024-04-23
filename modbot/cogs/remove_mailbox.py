import discord
from discord.ext import commands
from modbot.database.mailbox_utils import remove_mailbox, remove_all_mailboxes
from modbot.database.models import Mailbox
from modbot.database.emails_utils import EmailsUtils

class RemoveMailbox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def remove_mailbox(self, ctx: commands.Context, *args):
        channel = ctx.channel
        def channel_check(m):
            return m.author != self.bot.user and m.channel == channel
        if len(args) < 1:
            await channel.send("Usage: !remove_mailbox <mailbox_address>")
            return
        mailbox_address = args[0]
        remove_mailbox(mailbox_address)
        await channel.send(f"Removed mailbox {mailbox_address} successfully")
    @commands.command()
    async def remove_all_mailboxes(self, ctx: commands.Context):
        channel = ctx.channel
        remove_all_mailboxes(ctx.guild.id)
        await channel.send(f"Removed all mailboxes successfully")
async def setup(bot):
    await bot.add_cog(RemoveMailbox(bot))
        

    
