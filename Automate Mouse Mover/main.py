import pyautogui
import time
import keyboard
import random

print("Please Hold q if you want to quit")
print("How long would you like to have between mouse position changes?", end=" ")
posMoveTime = input()
while not posMoveTime.isdigit():
    print("Invalid input. Please try again!", end=" ")
    posMoveTime = input()
print(pyautogui.position())  # print the position of the current cursor

while True:
    if keyboard.is_pressed("q"):
        print("q is pressed")
        break
    else:
        # print("I AM HERE")
        pyautogui.moveTo(random.randint(2000, 3000), random.randint(300, 500), 1)  # Moves mouse to a random position
        time.sleep(int(posMoveTime))
        # print(pyautogui.position())
