import discord
from discord.ext import commands
from modbot.database.mailbox_utils import add_mailbox
from modbot.database.models import Mailbox
from modbot.database.emails_utils import EmailsUtils

class AddMailbox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add_mailbox(self, ctx: commands.Context):
        channel = ctx.channel

        def channel_check(m):
            return m.author != self.bot.user and m.channel == channel

        await channel.send("Enter mailbox address:")
        msg = await self.bot.wait_for("message", check=channel_check)
        mailbox_address = msg.content
        await channel.send("Enter password:")
        msg = await self.bot.wait_for("message", check=channel_check)
        password = msg.content
        #Delete last 4 messages in the channel
        async for message in channel.history(limit=4):
            await message.delete()
        #get mails
        email_utils = EmailsUtils()

        


        # await channel.send(f"user entered: (mailbox_name: {mailbox_name}, password: {password})")

        try:
            add_mailbox(Mailbox(address=mailbox_address, password=password, guild_id=ctx.guild.id))
            await channel.send(f"Added mailbox " + mailbox_address + " successfully")
            mails = email_utils.get_emails(ctx.guild.id)
        except RuntimeError:
            await channel.send(f"Failed adding mailbox")




    @commands.command()
    async def ping(self, ctx):
        """Responds with 'pong'."""
        await ctx.send('pong')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        # You can react to messages with this listener
        # Remember not to handle commands here; discord.py does that automatically


async def setup(bot):
    await bot.add_cog(AddMailbox(bot))
