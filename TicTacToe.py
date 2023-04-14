import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader


def play(row, col):
    global player

    if player == 1:
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color: skyblue;")
        player = 2

    elif player == 2:
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color: orange;")
        player = 1

    check()


def check():
    if buttons[0][0].text() == "X" and buttons[0][1].text() == "X" and buttons[0][2].text() == "X":
        msg_box = QMessageBox(text="Player 1 win")
        msg_box.exec()


app = QApplication(sys.argv)


player = 1

loader = QUiLoader()
main_window = loader.load("episode18\main_window.ui")
main_window.show()

buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))

app.exec()
