#Selenium Webdriver must be installed for this to work
import time;
import pyautogui
import webbrowser
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver;

#application
def window():
    def runBot():
        click = int(clickInput.text())
        for i in range(click):
            link = linkInput.text()
            
            webbrowser.open('https://google.com')
            time.sleep(2)
            pyautogui.hotkey('command','shift','n')
            time.sleep(2)
            pyautogui.hotkey('command','l')
            pyautogui.typewrite(link)
            pyautogui.hotkey('enter')
            time.sleep(10)
            pyautogui.click(1160,160)
            time.sleep(6)
            # close tab
            time.sleep(2)
            pyautogui.click(70,10)
            pyautogui.click(70,275)
            time.sleep(2)
            #reopen tab
            time.sleep(2)
        
#------WINDOW------------
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 150)
    win.setWindowTitle("Add Fly Bot")

    linkLabel = QtWidgets.QLabel(win)
    linkLabel.setText("Link")
    linkLabel.move(15, 20)
    linkInput = QtWidgets.QLineEdit(win)
    linkInput.setGeometry(110, 10, 191, 20)
    linkInput.move(100, 25)

    clickLabel = QtWidgets.QLabel(win)
    clickLabel.setText("number of click")
    clickLabel.move(15, 45)
    clickInput = QtWidgets.QLineEdit(win)
    clickInput.setGeometry(40, 10, 40, 20)
    clickInput.move(140, 55)

    runBotBtn = QtWidgets.QPushButton(win)
    runBotBtn.setGeometry(60, 270, 180, 40)
    runBotBtn.move(65, 80)       
    runBotBtn.setText("RUN VIEWBOT")
    runBotBtn.clicked.connect(runBot)

    win.show()
    sys.exit(app.exec_())



window()