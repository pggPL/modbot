import argparse


def main():
    # Parse arg token from command line
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="Discord bot token")
    args = parser.parse_args()
    
    # Run bot
    bot = ModBot()
    bot.run(args.token)