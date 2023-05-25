import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import webbrowser
import requests


class Flickr_User(QtWidgets.QMainWindow):
    def __init__(self):
        super(Flickr_User, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Flickr')
        self.ui.lineEdit.setPlaceholderText('Username')
        self.ui.pushButton.clicked.connect(self.UserFinder)

    def UserFinder(self):
        api_key = "a41956e04d7c0581697c214c254631b5"

        # Запрос информации о пользователе по username
        username = self.ui.lineEdit.text()
        url = f"https://api.flickr.com/services/rest/?method=flickr.people.findByUsername&api_key={api_key}&username={username}&format=json&nojsoncallback=1"
        response = requests.get(url)
        data = response.json()

        # Получение ID пользователя
        user_id = data["user"]["id"]

        # Открытие профиля пользователя в браузере
        webbrowser.open(f"https://www.flickr.com/people/{user_id}/")


app = QtWidgets.QApplication([])
application = Flickr_User()
application.show()

sys.exit(app.exec())
