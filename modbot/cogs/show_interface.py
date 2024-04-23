from discord.ext import commands
from modbot.database.emails_utils import EmailsUtils
from modbot.database.models import Mail
from modbot.database.models import Mailbox
from modbot.cogs.add_mailbox import AddMailbox
from modbot.cogs.respond import Respond
import discord


class ShowInterface(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="show_interface")
    async def show_interface(self, ctx: commands.Context):
        """Show interface information"""
        # Code to show interface information
        channel = ctx.channel
        guild = ctx.guild
        email_utils = EmailsUtils()
        mails = email_utils.get_emails(ctx.guild.id)
        view = discord.ui.View()
        mail_index = 2
        #Add the button for adding mailbox
        async def add_mailbox_callback(interaction: discord.Interaction):
            await interaction.response.defer()
            add_mailbox_cog = AddMailbox(self.bot)
            await add_mailbox_cog.add_mailbox(self, ctx)
        async def previous_mail_callback(interaction: discord.Interaction):
            nonlocal mail_index
            if mail_index > 0:
                mail_index -= 1
            embed = Respond.embeded_message(mails[mail_index])
            await interaction.response.edit_message(embed=embed)
        async def next_mail_callback(interaction: discord.Interaction):
            nonlocal mail_index
            if mail_index < len(mails) - 1:
                mail_index += 1
            embed = Respond.embeded_message(mails[mail_index])
            await interaction.response.edit_message(embed=embed)
        async def respond_mail_callback(interaction: discord.Interaction):
            respond_obj = Respond(self.bot)
            await respond_obj.respond(respond_obj, ctx, mails[mail_index])
        view = Respond.add_sample_button(view, label='<', callback=previous_mail_callback)
        view = Respond.add_sample_button(view, label='>', callback=next_mail_callback)
        view = Respond.add_sample_button(view, label='Respond', callback=respond_mail_callback)
        view = Respond.add_sample_button(view, label = 'Add mailbox', callback = add_mailbox_callback)

        embed = Respond.embeded_message(mails[mail_index])
        await channel.send(view=view, embed=embed)


async def setup(bot):
    await bot.add_cog(ShowInterface(bot))