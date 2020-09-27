import requests
from PyQt5 import QtWidgets, QtCore
from clientui import Ui_MainWindow


class Messenger(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main messenger class"""
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.sendButton.pressed.connect(self.button_pressed)
        self.url = url
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)
        self.after_id = 0



    def button_pressed(self):
        """Describes the behavior of a send message button"""
        name = self.nameEdit.text()
        text = self.textEdit.toPlainText()
        data = {'name': name, 'text': text}
        response = None
        try:
            response = requests.post(self.url + '/send', json=data)
        except:
            pass
        if response and response.status_code:
            self.textEdit.clear()
            self.textEdit.repaint()
        else:
            self.messagesBrowser.append('При отправке сообщения произошла ошибка')
            self.messagesBrowser.repaint()


    def pretty_print(self, message):
        """Prints formatted message in application window"""
        print(message)
        dt = message[3]
        first_line = dt + '  ' + message[1]
        self.messagesBrowser.append(first_line)
        self.messagesBrowser.append(message[2])
        self.messagesBrowser.append('')
        self.messagesBrowser.repaint()


    def update_messages(self):
        """Getting messages and sending to print function"""
        response = None
        try:
            response = requests.get(self.url + '/messages', params={'after_id': self.after_id})
        except:
            pass
        if response and response.status_code == 200:
            messages = response.json()['messages']
            for message in messages:
                self.pretty_print(message)
                self.after_id = message[0]




app = QtWidgets.QApplication([])
window = Messenger('http://127.0.0.1:5000')
window.show()
app.exec_()
