import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QGridLayout, QPushButton, QLineEdit)
from PyQt5.QtCore import Qt


class BeigeCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор для неких эстетов")
        # Увеличиваем размер в 1.3 раза (оригинал 300x400)
        self.setFixedSize(int(400), int(600))

        # Центральный виджет и основной layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Поле для вывода
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            """
            font-size: 28px; 
            border: 2px solid #d2b48c;
            padding: 8px;
            background-color: #f5f5dc;
            color: #5a4a3a;
            """
        )
        self.display.setFixedHeight(80)
        main_layout.addWidget(self.display)

        # Кнопки калькулятора
        buttons_layout = QGridLayout()
        buttons_layout.setSpacing(10)  # Увеличиваем промежутки между кнопками
        main_layout.addLayout(buttons_layout)

        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '⌫',
            '1', '2', '3', '-', '√',
            '0', '.', '=', '+', 'x²'
        ]

        # Создание и размещение кнопок
        for i, text in enumerate(buttons):
            button = QPushButton(text)
            button.setStyleSheet(
                """
                QPushButton {
                    font-size: 22px;
                    padding: 15px;
                    border: 1px solid #d2b48c;
                    background-color: #f5f5dc;
                    color: #5a4a3a;
                    min-width: 60px;
                    min-height: 60px;
                }
                QPushButton:hover {
                    background-color: #e6d8b5;
                }
                """
            )
            button.clicked.connect(self.on_button_click)

            # Особые стили для функциональных кнопок
            if text in {'=', 'C', '⌫'}:
                button.setStyleSheet(
                    """
                    QPushButton {
                        font-size: 22px;
                        padding: 15px;
                        border: 1px solid #d2b48c;
                        background-color: #d2b48c;
                        color: white;
                        min-width: 60px;
                        min-height: 60px;
                    }
                    QPushButton:hover {
                        background-color: #c19a6b;
                    }
                    """
                )

            row = i // 5
            col = i % 5
            buttons_layout.addWidget(button, row, col)

        self.setStyleSheet("background-color: #f5f5dc;")

    def on_button_click(self):
        button = self.sender()
        text = button.text()
        current_text = self.display.text()

        if text == 'C':
            self.display.clear()
        elif text == '⌫':
            self.display.backspace()
        elif text == '=':
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except:
                self.display.setText("Не-не, давай другое")
        elif text == '√':
            try:
                result = eval(current_text) ** 0.5
                self.display.setText(str(result))
            except:
                self.display.setText("Что??")
        elif text == 'x²':
            try:
                result = eval(current_text) ** 2
                self.display.setText(str(result))
            except:
                self.display.setText("Ты серьёзно?")
        else:
            self.display.setText(current_text + text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = BeigeCalculator()
    calc.show()
    sys.exit(app.exec_())