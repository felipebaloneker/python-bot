import pyautogui
import webbrowser
import time 
import json
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver;

file = open('accounts.json')
data = json.load(file)

def window():
    def runBot():
        link = linkInput.text()
        for i in data['values']:
            print(i['name'])
            # open browser
            webbrowser.open('https://google.com')
            time.sleep(2)
            # Open anonimus tab
            pyautogui.hotkey('command','shift','n')
            time.sleep(2)
            # Open youtube
            pyautogui.hotkey('command','l')
            pyautogui.typewrite('https://www.youtube.com')
            pyautogui.hotkey('enter')
            time.sleep(2)
            # Sigin youtube
            pyautogui.click(1200,160, duration=2)
            time.sleep(2)
            pyautogui.click(600,400)
            time.sleep(2)
            pyautogui.typewrite(i['name'])
            pyautogui.hotkey('enter')
            time.sleep(4)
            pyautogui.typewrite(i['password'])
            pyautogui.hotkey('enter')
            time.sleep(3)
            # Open link
            pyautogui.hotkey('command','l')
            pyautogui.typewrite(link)
            pyautogui.hotkey('enter')
            time.sleep(3)
            # subscribe chanel
            pyautogui.click(1150,245)
            time.sleep(3)
            # close tab
            pyautogui.click(70,10)
            pyautogui.click(70,275)
            time.sleep(2)
            #reopen tab
            webbrowser.open('https://google.com')
            time.sleep(5)


    
#------WINDOW------------
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 150)
    win.setWindowTitle("YouTube LikeBot")

    linkLabel = QtWidgets.QLabel(win)
    linkLabel.setText("Video Link")
    linkLabel.move(15, 20)
    linkInput = QtWidgets.QLineEdit(win)
    linkInput.setGeometry(110, 10, 191, 20)
    linkInput.move(100, 25)

    runBotBtn = QtWidgets.QPushButton(win)
    runBotBtn.setGeometry(60, 270, 180, 40)
    runBotBtn.move(65, 80)       
    runBotBtn.setText("RUN VIEWBOT")
    runBotBtn.clicked.connect(runBot)

    win.show()
    sys.exit(app.exec_())



window()