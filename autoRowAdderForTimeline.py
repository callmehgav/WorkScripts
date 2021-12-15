import time
import threading
import string
import random
import numpy as np
from pynput.mouse import Button as pyB, Controller
from pynput.keyboard import Listener, KeyCode, Key, Controller as C
from time import sleep
from tkinter import *

counter =0
everyMinute = 60
buttonLeftClick = pyB.left
buttonRightClick = pyB.right
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='+')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        print("running")
        self.delay = delay
        self.button = button
        self.running = True
        self.program_running = True

    def start_clicking(self):
        print("Started Clicking")
        self.running = True

    def stop_clicking(self):
        print("Stopped Clicking")
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                randomNameBot(self)
  






def randomNameBot(self):
    
    time.sleep(2)
    #move mouse to the first button press location
    moveMouse(40,159)
    time.sleep(.5)
    mouse.click(self.button)
    time.sleep(.5)
    #move mouse down to add line
    #the following line will get commented out after the screen is full
    #moveMouse(40,215)
    time.sleep(.5)
    mouse.click(self.button)
    time.sleep(2)
    #type random string
    for x in range(returnInt(1,10)):
        char = random.choice("abcdefghijklmnopqrstuvwxyz#-_)(*&^%$@!")
        keyboard.press(char)
        keyboard.release(char)
    time.sleep(.5)
    for x in range(10):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(.2)
    #press space
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(.5)
    #readjust mouse to info line spot
    moveMouse(40,159)
    #repeat
    
    

def returnInt (minInt, maxInt):
    return np.random.randint(minInt, maxInt)

def moveMouse(x,y):
    mouse.position = (x, y)
    
def click():
    cm = ClickMouse()
    if self.running == True:
        cm.stop_clicking()
    else:
        cm.start_clicking()

keyboard = C()
mouse = Controller()
click_thread = ClickMouse(1, buttonLeftClick)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
