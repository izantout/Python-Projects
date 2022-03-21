import time
import keyboard
import pyautogui
import win32api
import win32con


# time.sleep(2)
# print(pyautogui.position())
# position 1: x=1028 y = 1700
# position 2: x=1260 y = 1700
# position 3: x=1466 y = 1700
# position 4: x=1684 y = 1700

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0275)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):
    if pyautogui.pixel(1028, 1700)[0] == 0:
        click(1028, 1700)
    if pyautogui.pixel(1260, 1700)[0] == 0:
        click(1260, 1700)
    if pyautogui.pixel(1466, 1700)[0] == 0:
        click(1466, 1700)
    if pyautogui.pixel(1684, 1700)[0] == 0:
        click(1684, 1700)
