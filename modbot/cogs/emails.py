from discord.ext import commands
from modbot.database.emails_utils import EmailsUtils


class EmailsTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emails_db_utils = EmailsUtils()

    #Make the bot say hello to the user on every channel on the server
    @commands.command(aliases=['show_mails'])
    async def show_emails(self, ctx: commands.Context):
        """Shows all emails received to the mailboxes
           associated with the guild"""

        #FIXME: get emails from the database instead of placeholders
        emails = self.emails_db_utils.get_emails(ctx.guild.id)

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
