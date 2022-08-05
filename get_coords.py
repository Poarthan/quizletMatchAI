#!/usr/bin/env python3

import pyautogui, sys
import mouse
from pynput.mouse import Listener
from pynput import keyboard
import time


def main():
    truncate="N"
    truncate = input("Are you sure you want to clear the coords file (Y or N)?")
    if truncate=="y" or truncate == "Y":
        f=open("coordfile.txt", "a")
        f.truncate(0)
        f.close()

    print("Press s to start reccording coordinates, press CTRL-C in the terminal to stop program")

    begin()
def begin():
    def on_press(key):
        #try:
        if key.char == "s":
            print("starting")
            start()
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

def on_click(x, y, button, pressed):
    if pressed:
        print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        f=open("coordfile.txt", "a")
        f.write(str(x))
        f.write(",")
        f.write(str(y))
        f.write("\n")
        f.close()
def start():
    with Listener(on_click=on_click) as listener:
        listener.join()


if __name__ == '__main__':
    main()
