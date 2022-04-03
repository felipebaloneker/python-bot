import pyautogui
import webbrowser
import time 
import json

def window():
    def runBot():
        file = open('accounts.json')
        data = json.load(file)
        link = linkInput.text()

        for i in data['values']:
            print(i["name"])
            webbrowser.open('https://google.com')
            time.sleep(2)

            pyautogui.hotkey('command','shift','n')

            pyautogui.click(408,80, duration=3)

            pyautogui.typewrite('https://www.youtube.com')
            time.sleep(5)
            pyautogui.hotkey('enter')

            time.sleep(5)
            pyautogui.click(700,160, duration=2)
            time.sleep(8)
            pyautogui.click(600,400)
            time.sleep(6)
            pyautogui.typewrite(i['name'])
            pyautogui.hotkey('enter')
            time.sleep(6)
            pyautogui.typewrite(i['password'])
            pyautogui.hotkey('enter')
            time.sleep(6)
            pyautogui.click(486,633)
            time.sleep(8)
            pyautogui.click(408,80, duration=3)
            pyautogui.typewrite(link)
            time.sleep(8)
            pyautogui.click(305,680)
            time.sleep(6)
            pyautogui.hotkey('command','q')
            time.sleep(1)
            pyautogui.hotkey('command','q')


    
#------WINDOW------------
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 150)
    win.setWindowTitle("YouTube ViewBot")

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