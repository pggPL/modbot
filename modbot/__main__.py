import argparse
import asyncio

import discord

from modbot.modbot import bot


async def load_extensions(bot_object, extensions):
    for extension in extensions:
        await bot_object.load_extension(extension)


def main():
    # Parse arg token from command line
    parser = argparse.ArgumentParser()
    # arg with flag --token-file
    parser.add_argument('--token-file', type=str, help='path to file with token')

    args = parser.parse_args()
    token_file = args.token_file

    # default to "token.txt"
    if token_file is None:
        token_file = "token.txt"

    # get token
    with open(token_file, 'r') as f:
        token = f.read().strip()

    intents = discord.Intents.all()
    intents.message_content = True

    # Load extensions (cogs)
    initial_extensions = ['modbot.cogs.add_mailbox', 'modbot.cogs.show_mailboxes',
                          'modbot.cogs.emails', 'modbot.cogs.show_interface', 'modbot.cogs.respond', 'modbot.cogs.remove_mailbox']
    asyncio.run(load_extensions(bot, initial_extensions))
    #Create a new channel and send a message

    bot.run(token)
