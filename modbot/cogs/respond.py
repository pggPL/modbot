from discord.ext import commands
import discord
from modbot.database.emails_utils import EmailsUtils
from modbot.database.models import Mail

class Respond(commands.Cog):
    @staticmethod
    def embeded_message(message: Mail):
        #Show the title and the sender,then show the content
        embed = discord.Embed(title="From " + message.sender_address, description="", color=0x00ff00)
        #Add the mail
        embed.add_field(name='Subject: ' + message.subject, value=message.content, inline=False)
        return embed
    
    @staticmethod
    def add_sample_button(view, label='Sample Button', callback=None):
        #Create a button with callback
        button = discord.ui.Button(label=label, style=discord.ButtonStyle.primary)
        button.callback = callback
        view.add_item(button)
        return view
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def respond(self, ctx: commands.Context, *args):
        channel = ctx.channel
        if len(args) < 1:
            await channel.send("Usage: !respond <mail_id> <message>")
            return
        mail = args[0]

        await channel.send(f"Enter subject for response for {mail.mail_id}")
        msg = await self.bot.wait_for("message", check=lambda m: m.author != self.bot.user and m.channel == channel)
        subject = msg.content
        await channel.send(f"Enter message for response for {mail.mail_id}")
        msg = await self.bot.wait_for("message", check=lambda m: m.author != self.bot.user and m.channel == channel)
        content = msg.content
        view = discord.ui.View()

        async def respond_mail_callback(interaction: discord.Interaction):
            nonlocal view
            await interaction.channel.send(f"Responding to {mail.mail_id} with subject {subject} and content {content}")
            #Remove the buttons
            view = view.clear_items()
            #Edit the message
            embed = self.embeded_message(mail)
            await interaction.response.edit_message(view = view, embed=embed)
            #Run command "show_interface"
            await self.bot.get_command('show_interface').callback(self.bot,ctx)
        async def reject_response_callback(interaction: discord.Interaction):
            nonlocal view
            await interaction.channel.send("Response rejected")
            #Remove the buttons
            view = view.clear_items()
            #Edit the message
            embed = self.embeded_message(mail)
            await interaction.response.edit_message(view = view, embed=embed)

        view = self.add_sample_button(view, label='✓', callback=respond_mail_callback)
        view = self.add_sample_button(view, label='X', callback=reject_response_callback)
        response_mail = Mail(subject=subject, content=content, sender_address=mail.sender_address, receiver_address=mail.sender_address)
        embed = self.embeded_message(response_mail)
        await channel.send(view=view, embed=embed)
async def setup(bot):
    await bot.add_cog(Respond(bot))

    