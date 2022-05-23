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
            name = i['name'].split("@")
            # open browser
            webbrowser.open('https://google.com')
            time.sleep(2)
            # Open anonimus tab
            pyautogui.hotkey('command','shift','n')
            time.sleep(2)

            # Open instagram
            pyautogui.hotkey('command','l')
            pyautogui.typewrite('https://www.instagram.com')
            pyautogui.hotkey('enter')
            time.sleep(8)
            pyautogui.click(915,600)
            time.sleep(5)
            pyautogui.click(600,400)
            pyautogui.typewrite(i['name'])
            pyautogui.hotkey('tab')
            pyautogui.typewrite(name)
            pyautogui.hotkey('tab')
            pyautogui.typewrite(name[0:5])
            pyautogui.click(750,490)
            pyautogui.hotkey('tab')
            pyautogui.typewrite(i['password'])
            pyautogui.hotkey('enter')
            time.sleep(5)

            #add birthday
            pyautogui.click(725,400)
            pyautogui.hotkey('1')      
            pyautogui.hotkey('enter')      
            pyautogui.click(640,500)
            time.sleep(3)

            # Open gmail and get code
            pyautogui.hotkey('command','t')
            time.sleep(2)
            pyautogui.hotkey('command','l')
            pyautogui.typewrite('https://www.google.com/')
            pyautogui.hotkey('enter')
            time.sleep(3)
            pyautogui.click(1180,165)
            time.sleep(3)
            pyautogui.typewrite(i['name'])
            pyautogui.hotkey('enter')
            time.sleep(3)
            pyautogui.typewrite(i['password'])
            pyautogui.hotkey('enter')
            time.sleep(3)
            pyautogui.click(1170,160)
            time.sleep(8)
            pyautogui.click(580,160)
            pyautogui.typewrite('instagram')
            time.sleep(2)
            pyautogui.click(590,310)
            time.sleep(2)
            pyautogui.moveTo(760,630)
            pyautogui.click(button='right')
            pyautogui.click(830,608)
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            time.sleep(2)
            pyautogui.click(630,390)
            pyautogui.hotkey('command', 'v')
            pyautogui.click(630,440)



            # get like
            pyautogui.click(800, 760)
            # close tab
            pyautogui.click(70,10)
            pyautogui.click(70,275)
            time.sleep(2)
            #reopen tab
            time.sleep(2)


    
#------WINDOW------------
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 150)
    win.setWindowTitle("Instagram Singup")

    linkLabel = QtWidgets.QLabel(win)
    linkLabel.setText("Post Link")
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