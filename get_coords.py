#!/usr/bin/env python3

import pyautogui, sys
import mouse
from pynput.mouse import Listener


def on_click(x, y, button, pressed):
    if pressed:
        print ('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

with Listener(on_click=on_click) as listener:
    listener.join()
