# from modbot.database import get_server_name, set_server_name
# from modbot.templates import render_template


# async def first_message(guild):
#     if get_server_name(guild.id) is None:
#         channel = await guild.create_text_channel('modbot-configuration')
#         await channel.send(render_template('configuration/message1.md'))
#
#
# async def reset_configuration(ctx):
#     # check if context channel is modbot-configuration
#     if ctx.channel.name != 'modbot-configuration':
#         await ctx.send('You can only reset configuration in modbot-configuration channel!')
#         return
#     set_server_name(ctx.guild.id, None)
#
#     # remove all configuration channels
#     for channel in ctx.guild.channels:
#         if channel.name.startswith('modbot-configuration'):
#             await channel.purge()
#             # if channel is not last, remove it
#             if channel != ctx.channel:
#                 await channel.delete()
#     await ctx.channel.send(render_template('configuration/message1.md'))