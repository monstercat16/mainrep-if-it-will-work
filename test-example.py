from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Создаем элементы интерфейса
        self.textarea = QTextEdit()
        self.canvas_layout = QVBoxLayout()
        self.canvas_scroll_area = QScrollArea()
        self.canvas_widget = QWidget()
        self.canvas_widget.setLayout(self.canvas_layout)
        self.canvas_scroll_area.setWidgetResizable(True)
        self.canvas_scroll_area.setWidget(self.canvas_widget)

        # Создаем главный layout и добавляем на него элементы
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.textarea)
        self.layout.addWidget(self.canvas_scroll_area)

        # Устанавливаем главный layout
        self.setLayout(self.layout)

        # Добавляем возможность перетаскивания файлов на окно приложения
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        # Проверяем, что перетаскивается файл изображения
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Получаем изображение из события
        image = QImage(event.mimeData().imageData())

        # Если изображение загружено успешно, отображаем его на canvas
        if not image.isNull():
            canvas_item = QLabel()
            pixmap = QPixmap.fromImage(image)
            canvas_item.setPixmap(pixmap)
            self.canvas_layout.addWidget(canvas_item)

    def keyPressEvent(self, event):
        # Обрабатываем нажатия клавиш сочетаний
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_O:
            # Открываем диалоговое окно выбора файла и загружаем изображение на canvas
            file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать изображение", "", "Images (*.png *.xpm *.jpg)")
            if file_path:
                canvas_item = QLabel()
                pixmap = QPixmap(file_path)
                canvas_item.setPixmap(pixmap)
                self.canvas_layout.addWidget(canvas_item)
        else:
            super().keyPressEvent(event)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()