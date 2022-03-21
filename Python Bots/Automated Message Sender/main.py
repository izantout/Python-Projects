import pyautogui, time
time.sleep(10)
SPAM = open("file", "r")
for word in SPAM:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
