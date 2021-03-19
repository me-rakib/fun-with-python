import pyautogui
import time
msg = pyautogui.prompt(text='Enter text here', title="Message Box", default="Hello World")
for i in range(100):
    if i == 1:
        time.sleep(10)
    else:
        pyautogui.typewrite(msg)
        pyautogui.press('enter')