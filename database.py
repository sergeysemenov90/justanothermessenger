import psycopg2

DBNAME = 'my_database'
USER = 'postgres'
with open('password.txt', 'r', encoding='utf-8-sig') as file:
    PASSWORD = file.read().rstrip()
HOST = 'localhost'
connection = psycopg2.connect(dbname=DBNAME, user=USER,
                              password=PASSWORD, host=HOST)
connection.autocommit = True



def savetodb(message):
    """Saving messages to database"""
    cursor = connection.cursor()
    cursor.execute('insert into public.messages (name, mes_text, mes_time) values (%s, %s, %s)', (message['name'], message['text'], message['time']))


def getfromdb(after_id = 0):
    """Getting messages from database"""
    cursor = connection.cursor()
    cursor.execute('select * from public.messages where id > %d' %after_id)
    rows = cursor.fetchall()
    return rows
