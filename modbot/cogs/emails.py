from discord.ext import commands
from modbot.database.emails_utils import get_emails


class EmailsTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['show_mails'])
    async def show_emails(self, ctx: commands.Context):
        """Shows all emails received to the mailboxes
           associated with the guild"""

        emails = get_emails(ctx.guild.id)

        result = ""

        for email in emails:
            result += email.dc_show()
            result += '\n'

        if result:
            await ctx.channel.send(result)
        else:
            await ctx.channel.send("No mails found sent to mailboxes associated with the guild")

async def setup(bot):
    await bot.add_cog(EmailsTools(bot))
