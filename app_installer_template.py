import sys, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = "Python Installer Template" # Change with your app's name
    self.left = 0
    self.top = 0
    self.width = 800 # Window width
    self.height = 600 # Window height
    self.initUI()

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    self.layout = QVBoxLayout(self)

    self.appNameLabel = QLabel("Python App Installer", self) # Replace with app's name
    self.appNameLabel.move(50, 40)
    self.appNameLabel.resize(700, 30)
    self.appNameLabel.setStyleSheet("font-size: 25px")

    self.appicn = QPixmap("icon.png") # App's icon | 128x128, 96x96, 64x64
    self.appIcon = QLabel(self)
    self.appIcon.setPixmap(self.appicn)
    self.appIcon.move(670, -10)
    self.appIcon.resize(128, 128) # Icon size

    # Description of your app
    # Write description inside box below
    self.appDesc = QLabel("""
+-------------------------------------------------------------------------------------------+
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
|                                                                                           |
+-------------------------------------------------------------------------------------------+
    """, self)
    self.appDesc.move(30, 50)
    self.appDesc.resize(800, 500)

    self.author = QLabel("Author", self)
    self.author.move(30, 560)
    self.author.resize(400, 20)
    self.author.setStyleSheet("color: aqua") # Set your own color

    self.installButton = QPushButton("Install", self)
    self.installButton.move(500, 540)
    self.installButton.clicked.connect(self.installScreen)

    self.cancelButton = QPushButton("Cancel", self)
    self.cancelButton.move(630, 540)
    self.cancelButton.clicked.connect(self.appExit)

    self.setLayout(self.layout)
    self.show()

  def appExit(self):
    sys.exit()

  def installScreen(self):
    self.appDesc.hide()
    self.installButton.hide()

    self.currAction = QLabel("Current Action", self) # Label that shows what the installer actually does
    self.currAction.move(60, 270)
    self.currAction.resize(300, 30)
    self.currAction.setStyleSheet("color: gray")
    self.currAction.show()

    self.insProgress = QProgressBar(self)
    self.insProgress.move(50, 300)
    self.insProgress.resize(700, 30)
    self.insProgress.show()

    for i in range(101):
      time.sleep(0.01) # Change with your delay
      self.insProgress.setValue(i)
      if i < 10:                              # Replace with your own values
        self.currAction.setText("Preparing")  # Replace with your own texts
      elif i <= 30:
        self.currAction.setText("Unpacking")
      elif i <= 50:
        self.currAction.setText("Installing")
      elif i <= 90:
        self.currAction.setText("Almost done...")

    self.currAction.setText("Done")
    self.installButton.setText("Done")
    self.installButton.clicked.disconnect()
    self.installButton.clicked.connect(self.installationDone)
    self.installButton.show()

  def installationDone(self):
    self.installButton.clicked.disconnect()
    self.installButton.clicked.connect(self.appExit)
    self.currAction.hide()
    self.insProgress.hide()
    self.cancelButton.hide()

    self.thanksLabel = QLabel("Thanks for installing <app name>", self) # Replace <app name> with your app name 
                                                                  # Optionally replace the text with your own
    self.thanksLabel.move(100, 150)
    self.thanksLabel.resize(300, 300)
    self.thanksLabel.setStyleSheet("font-size: 15px")
    self.thanksLabel.show()

if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    ex = App()
    app.exec_()
