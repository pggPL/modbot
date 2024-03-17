import argparse

import discord

from modbot.modbot import bot


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
    
    
    bot.run(token)