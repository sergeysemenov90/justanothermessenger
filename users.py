import psycopg2

DBNAME = 'my_database'
USER = 'postgres'
PASSWORD = '7PF6wihk'
HOST = 'localhost'


class User():
    def __init__(self):
        pass


    def savetodb(self):
        self.name = input('Введите ваше имя:')
        self.surname = input('Введите вашу фамилию:')
        self.birth = input('Введите вашу дату рождения:')
        user_tuple = (self.name, self.surname, self.birth)
        connection = psycopg2.connect(dbname=DBNAME, user=USER,
                        password=PASSWORD, host=HOST)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO peoples (name, surname, birth) VALUES {user_tuple};")
        connection.close()
        # a = cursor.execute("SELECT * FROM peoples;")
        # a = list(a)
        # print(a)

# serega = User()
# serega.savetodb()
