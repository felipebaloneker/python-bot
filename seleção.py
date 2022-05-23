import pyautogui
import time
pyautogui.moveTo(760,630)
pyautogui.click(button='right')
pyautogui.click(830,608)
time.sleep(2)
pyautogui.hotkey('ctrl', 'shift', 'tab')