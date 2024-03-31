import sqlite3


# def init():
#     db_conn = sqlite3.connect('mybot.db')
#     cursor = db_conn.cursor()
#
#     with open('./modbot/database/schema.sql', 'r') as f:
#         cursor.executescript(f.read())
#
#
# def get_server_name(guild_id):
#     db_conn = sqlite3.connect('mybot.db')
#     cursor = db_conn.cursor()
#
#     cursor.execute('SELECT server_name FROM servers WHERE server_id = ?', (guild_id,))
#     result = cursor.fetchone()
#
#     if result is None:
#         return None
#
#     return result[0]
#
# def set_server_name(guild_id, server_name):
#     db_conn = sqlite3.connect('mybot.db')
#     cursor = db_conn.cursor()
#
#     cursor.execute('INSERT OR REPLACE INTO servers (server_id, server_name) VALUES (?, ?)', (guild_id, server_name))
#     db_conn.commit()