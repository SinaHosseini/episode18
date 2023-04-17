import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader


def game_mode(type):
    global game_status
    if main_window.btn_pvp.isChecked():
        game_status = "PvP"

    elif main_window.btn_coop.isChecked():
        game_status = "Co-op"


def play(row, col):
    global player

    if game_status == "PvP":
        if player == 1:
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: skyblue;")
            player = 2

        elif player == 2:
            buttons[row][col].setText("O")
            buttons[row][col].setStyleSheet("color: orange;")
            player = 1

    if game_status == "Co_op":
        if player == 1:
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: skyblue;")
            player = 2

        elif player == 2:
            while True:
                rand_row = random.randint(0, 2)
                rand_col = random.randint(0, 2)
                if buttons[rand_row][rand_col].text() == "":
                    buttons[rand_row][rand_col].setText("O")
                    buttons[rand_row][rand_col].setStyleSheet("color: orange;")
                    player = 1
                    break

    check()


def new_game():
    global player
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText(" ")
            buttons[i][j].setStyleSheet("background: rgb(0, 0, 127);")
            player = 1


def about():
    msg_about_box = QMessageBox(text="""Welcome to Tic Tac Toe Game
    -You can play in PvP and Co-op modes with the computer or your friend.
    -New Game button is for reset game,
    -Also you can see your score in score board.""")
    msg_about_box.exec()


def check():
    global player, player1_score, player2_score, tie

    counter_X = 0
    counter_O = 0
    tie_status = True

    for i in range(3):
        sum_X = 0
        sum_O = 0
        for j in range(3):
            if buttons[i][j].text() == "X":
                sum_X += 1
                counter_X += 1

            elif buttons[i][j].text() == "O":
                sum_O += 1
                counter_O += 1

        if sum_X == 3:
            player1_score += 1
            main_window.your_score_box.setText(
                "Your score: " + str(player1_score))
            msg_box = QMessageBox(text="Player 1 win")
            msg_box.exec()
            tie_status = False

        elif sum_O == 3:
            player2_score += 1
            main_window.competitor_score_box.setText(
                "Competitor: " + str(player2_score))
            msg_box = QMessageBox(text="Player 2 win")
            msg_box.exec()
            tie_status = False

    for i in range(3):
        sum_X = 0
        sum_O = 0
        for j in range(3):
            if buttons[j][i].text() == "X":
                sum_X += 1

            elif buttons[j][i].text() == "O":
                sum_O += 1

        if sum_X == 3:
            player1_score += 1
            main_window.your_score_box.setText(
                "Your score: " + str(player1_score))
            msg_box = QMessageBox(text="Player 1 win")
            msg_box.exec()
            tie_status = False

        elif sum_O == 3:
            player2_score += 1
            main_window.competitor_score_box.setText(
                "Competitor: " + str(player2_score))
            msg_box = QMessageBox(text="Player 2 win")
            msg_box.exec()
            tie_status = False

    if buttons[0][0].text() == "X" and buttons[1][1].text() == "X" and buttons[2][2].text() == "X":
        player1_score += 1
        main_window.your_score_box.setText(
            "Your score: " + str(player1_score))
        msg_box = QMessageBox(text="Player 1 win")
        msg_box.exec()
        tie_status = False

    elif buttons[0][0].text() == "O" and buttons[1][1].text() == "O" and buttons[2][2].text() == "O":
        player2_score += 1
        main_window.competitor_score_box.setText(
            "Competitor: " + str(player2_score))
        msg_box = QMessageBox(text="Player 2 win")
        msg_box.exec()
        tie_status = False

    elif buttons[0][2].text() == "X" and buttons[1][1].text() == "X" and buttons[2][0].text() == "X":
        player1_score += 1
        main_window.your_score_box.setText(
            "Your score: " + str(player1_score))
        msg_box = QMessageBox(text="Player 1 win")
        msg_box.exec()
        tie_status = False

    elif buttons[0][2].text() == "O" and buttons[1][1].text() == "O" and buttons[2][0].text() == "O":
        player2_score += 1
        main_window.competitor_score_box.setText(
            "Competitor: " + str(player2_score))
        msg_box = QMessageBox(text="Player 2 win")
        msg_box.exec()
        tie_status = False

    if counter_X == 5 and counter_O == 4:
        if tie_status == True:
            tie += 1
            main_window.tie_box.setText("Tie: " + str(tie))
            msg_box = QMessageBox(text="  Tie")
            msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = 1
    player1_score = 0
    player2_score = 0
    tie = 0

    loader = QUiLoader()
    main_window = loader.load("episode18\main_window.ui")
    main_window.show()

    buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
               [main_window.btn_4, main_window.btn_5, main_window.btn_6],
               [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

    for i in range(3):
        for j in range(3):
            buttons[i][j].clicked.connect(partial(play, i, j))

    main_window.btn_NG.clicked.connect(new_game)
    main_window.btn_about.clicked.connect(about)
    main_window.btn_pvp.clicked.connect(game_mode)
    main_window.btn_coop.clicked.connect(game_mode)

    app.exec()
