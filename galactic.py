import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

sga = [
	"a", "ᔑ",
	"b", "ʖ",
	"c", "ᓵ",
	"d", "↸",
	"e", "ᒷ",
	"f", "⎓",
	"g", "⊣",
	"h", "⍑",
	"i", "╎",
	"j", "⋮",
	"k", "ꖌ",
	"l", "ꖎ",
	"m", "ᒲ",
	"n", "リ",
	"o", "𝙹",
	"p", "!¡",
	"r", "∷",
	"s", "ᓭ",
	"t", "ℸ",
	"u", "⚍",
	"w", "∴",
	"v", "⍊",
	"x", " ̇/",
	"y", "||",
	"z", "⨅",
	"_", " "
]
class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = ""
		self.left = 100
		self.top = 100
		self.width = 640
		self.height = 140
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		self.inputText = QLineEdit("", self)
		self.inputText.setGeometry(20, 20, 600, 30)
		self.inputText.textChanged.connect(self.trl)

		self.output = QLineEdit("", self)
		self.output.setGeometry(20, 60, 600, 30)
		self.output.setReadOnly(True)

		self.decode = QCheckBox("Decode", self)
		self.decode.setGeometry(20, 100, 200, 30)

		self.show()

	def split(self, string):
		return [char for char in string]

	def trl(self):
		text = self.inputText.text()
		decoding = self.decode.isChecked()
		text = text.replace(" ", "_")
		out = ""
		letters = self.split(text)
		for i in range(len(text)):
			for l in range(len(sga)):
				if text[i] == sga[l]:
					if decoding == False:
						out += sga[l + 1]
					else:
						if sga[l + 1] == " ":
							out += " "
						else:
							out += sga[l - 1]

		self.output.setText(out)

if __name__ == "__main__":
	app = QApplication.instance()
	if app is None:
		app = QApplication(sys.argv)

	ex = App()
	app.exec_()