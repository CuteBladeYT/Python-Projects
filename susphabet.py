import os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Rune Translator"
        self.left = 0
        self.top = 0
        self.width = 600
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QVBoxLayout()

        def addw(w):
            layout.addWidget(w)

        self.tText = QLineEdit("", self)
        self.tText.move(10, 40)
        self.tText.resize(580, 30)
        addw(self.tText)

        eBtn = QPushButton("Encode", self)
        eBtn.move(50, ((40 + 30) + 20))
        addw(eBtn)

        dBtn = QPushButton("Decode", self)
        dBtn.move((50 + (40 + 30 + 20)) + 20, (40 + 30 + 20))
        addw(dBtn)

        cBtn = QPushButton("Clear", self)
        cBtn.move(400, (40 + 30 + 20))
        addw(cBtn)

        self.rune = QLineEdit("Output", self)
        self.rune.move(50, ((40 + 30 + 20 + 50)))
        self.rune.resize(500, 30)
        addw(self.rune)


        eBtn.clicked.connect(self.encode)
        dBtn.clicked.connect(self.decode)
        cBtn.clicked.connect(self.clearIO)


        self.setLayout(layout)

        self.show()

    def clearIO(self):
        self.rune.setText("Output")
        self.tText.setText("")

    def split(text):
        return [char for char in text]

    def trl(null, letter, mode):
        if mode == 0:
            if letter == "a" or letter == "A":
                return "ᚨ"
            if letter == "b" or letter == "B":
                return "ᛒ"
            if letter == "c" or letter == "C":
                return "ᚲ"
            if letter == "d" or letter == "D":
                return "ᛞ"
            if letter == "e" or letter == "E":
                return "ᛖ"
            if letter == "f" or letter == "F":
                return "ᚠ"
            if letter == "g" or letter == "G":
                return "ᚷ"
            if letter == "h" or letter == "H":
                return "ᚺ"
            if letter == "i" or letter == "I":
                return "ᛁ"
            if letter == "j" or letter == "J":
                return "ᛃ"
            if letter == "k" or letter == "K":
                return "ᚴ"
            if letter == "l" or letter == "L":
                return "ᛚ"
            if letter == "m" or letter == "M":
                return "ᛗ"
            if letter == "n" or letter == "N":
                return "ᚾ"
            if letter == "o" or letter == "O":
                return "ᛟ"
            if letter == "p" or letter == "P":
                return "ᛈ"
            if letter == "r" or letter == "R":
                return "ᚱ"
            if letter == "s" or letter == "S":
                return "ᛋ"
            if letter == "t" or letter == "T":
                return "ᛏ"
            if letter == "u" or letter == "U":
                return "ᚢ"
            if letter == "w" or letter == "W":
                return "ᚹ"
            if letter == "v" or letter == "V":
                return "ᚡ"
            if letter == "x" or letter == "X":
                return "ᛪ"
            if letter == "y" or letter == "Y":
                return "ᚤ"
            if letter == "z" or letter == "Z":
                return "ᛉ"
            else:
                return letter
        else:
            if letter == "ᚨ":
                return "a"
            if letter == "ᛒ":
                return "b"
            if letter == "ᚲ":
                return "c"
            if letter == "ᛞ":
                return "d"
            if letter == "ᛖ":
                return "e"
            if letter == "ᚠ":
                return "f"
            if letter == "ᚷ":
                return "g"
            if letter == "ᚺ":
                return "h"
            if letter == "ᛁ":
                return "i"
            if letter == "ᛃ":
                return "j"
            if letter == "ᚴ":
                return "k"
            if letter == "ᛚ":
                return "l"
            if letter == "ᛗ":
                return "m"
            if letter == "ᚾ":
                return "n"
            if letter == "ᛟ":
                return "o"
            if letter == "ᛈ":
                return "p"
            if letter == "ᚱ":
                return "r"
            if letter == "ᛋ":
                return "s"
            if letter == "ᛏ":
                return "t"
            if letter == "ᚢ":
                return "u"
            if letter == "ᚹ":
                return "w"
            if letter == "ᚡ":
                return "v"
            if letter == "ᛪ":
                return "x"
            if letter == "ᚤ":
                return "y"
            if letter == "ᛉ":
                return "z"
            else:
                return letter


    def encode(self):
        mode = 0
        print(self.tText.text())
        txt = self.tText.text()
        letters = [char for char in txt]
        out = ""
        for i in range(len(txt)):
            letter = letters[i]
            out += str(self.trl(letter, mode))
        print(out)
        self.rune.setText(out)

    def decode(self):
        mode = 1
        print(self.tText.text())
        txt = self.tText.text()
        letters = [char for char in txt]
        out = ""
        for i in range(len(txt)):
            letter = letters[i]
            out += str(self.trl(letter, mode))
        print(out)
        self.rune.setText(out)
#

if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    ex = App()
    app.exec_()
