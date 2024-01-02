import sqlite3
import discord


class MyBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_conn = sqlite3.connect('mybot.db')
        self.init_db()

    def init_db(self):
        cursor = self.db_conn.cursor()
        #cursor.execute('CREATE TABLE IF NOT EXISTS server_settings (guild_id INTEGER PRIMARY KEY, settings TEXT)')
        self.db_conn.commit()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        
        # tutaj powinien sprawdzić, w jakim stanie jest serwer
        # jeśli NOT_CONFIGURED, to utworzyć kanał ModBotCongiduration
        # i przejśc w odpowieni stan
        
        # jeśli jest skonfigurowany, to przejść w stan READY
        
        
    async def on_message(self, message):
        pass
    
    
    async def on_click(self, interaction):
        pass