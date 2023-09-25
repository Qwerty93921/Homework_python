from PyQt5 import QtWidgets # Создание виджетов(объектов-кнопки, надписи, формы и т.д.)
from PyQt5.QtWidgets import QApplication, QMainWindow # Создание приложения и ОКНА

import sys

# https://www.youtube.com/watch?v=LtgsjK2VnJg&list=PL0lO_mIqDDFXeDkOLHmEsL_HAEhw4-xDX&index=2
# Гоша Дударь
# Изучение PyQT (Python GUI) / Урок #2 – Библиотека PyQT5. Надписи и кнопки

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Простая программа") # Название ОКНА программы
        self.setGeometry(300, 250, 350, 200) # ПЕРВЫЕ 2 ЧИСЛА это ОТСТУП: ШИРИНА И ВЫСОТА от ВЕРХНЕЙ ЛЕВОЙ ТОЧКИ(ВПРАВО отступ на 300px, ОТ ВЕРХА отступ 250px)
        # ВТОРЫЕ 2 числа - это ШИРИНА И ВЫСОТА ОКНА ПРИЛОЖЕНИЯ(350px - ШИРИНА ОКНА приложения, 200px - ВЫСОТА ОКНА приложения)

        self.new_text = QtWidgets.QLabel(self) # Объект БУДЕТ ПОКАЗЫВАТЬСЯ ТОЛЬКО ПРИ НАЖАТИИ НА КНОПКУ

        # QLabel - создает текстовую надпись

        self.main_text = QtWidgets.QLabel(self) # В скобках писать К КАКОМУ ОКНУ будет ОТНОСИТЬСЯ НАДПИСЬ
        self.main_text.setText("Это базовая надпись") # Текст ВНУТРИ ТЕКСТОВОЙ НАДПИСИ
        self.main_text.move(100, 100) # Позволяет ДВИГАТЬ ПРЕДМЕТ ВНУТРИ ОКНА(ОТСТУП от ЛЕВА - 100px, от ВЕРХА - 100px, НО НЕ ОТ ВЕРХНЕГО ЛЕВОГО КРАЯ(ВЛК) МОНИТОРА, а ОТ ВЛК САМОГО ОКНА)
        self.main_text.adjustSize() # Он позволяет подстроить ШИРИНУ ОБЪЕКТА ПОД ЕГО СОДЕРЖИМОЕ(ЕСЛИ надпись НЕ ВЛЕЗАЕТ)

        self.btn = QtWidgets.QPushButton(self) # К какому окну оно будет относиться
        self.btn.move(70, 150) # Как MARGIN - от ЛЕВА ОТСТУП - 70px, ОТ ВЕРХА - 150px
        self.btn.setText("Нажми на меня")
        self.btn.setFixedWidth(200) # Ширина КНОПКИ - 200px
        self.btn.clicked.connect(self.add_label) # При нажатии кнопки вызывать метод ADD_LABEL, CONNECT - СОЕДИНЯЕТ НАЖАТИЕ С ФУНКЦИЕЙ 

    def add_label(self): # Функция для вывода ТЕКСТА ПОСЛЕ НАЖАТИЯ НА КНОПКУ
        # print("add") # Выводится текст в консоль
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()



# Далее нужна функция для создания проекта
def application():
    app = QApplication(sys.argv) # Сохранение настроек программы которые будут созранятся на компе
    window = Window() # Создание переменной для окна, в этой программе будет ТОЛЬКО 1 ОКНО

    window.show() # ВЫЗОВ окна
    sys.exit(app.exec_()) # Программа всегда будет правильно закрываться

if __name__ == "__main__": # Если файл является главным, тогда запускается функция application() которая запускает программу
    application()
