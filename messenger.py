from users import User
import time


class Messenger:
    db = []
    messages_count = 0
    def send_message(self,name, text):
        '''Отправка сообщений'''
        messagetime = time.asctime()
        self.db.append({'name' : name,
                        'time' : messagetime,
                        'text' : text})

    def get_message(self):
        '''Получение сообщений'''
        return self.db

    def get_new_message(self):
        '''Получение сообщений'''
        new_messages = self.db[self.messages_count:]
        self.messages_count += len(new_messages)
        return new_messages

messenger = Messenger()

messenger.send_message('Ivan','123')
messenger.send_message('Serega', 'Ого, осталось подключить БД')
print(f'Все сообщения - {messenger.get_message()}')
print(f'Новые сообщения - {messenger.get_new_message()}\n')

messenger.send_message('Ivan','первое новое сообщение')
messenger.send_message('Serega', 'второе новое сообщение')
print(f'Все сообщения - {messenger.get_message()}')
print(f'Новые сообщения - {messenger.get_new_message()}\n')

messenger.send_message('Ivan','третье новое сообщение')
messenger.send_message('Serega', 'четвертое новое сообщение')
print(f'Все сообщения - {messenger.get_message()}')
print(f'Новые сообщения - {messenger.get_new_message()}')
