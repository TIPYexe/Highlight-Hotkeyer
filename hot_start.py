import keyboard
import pygetwindow as gw
import time

active = gw.getActiveWindow()
OBS = gw.getWindowsWithTitle('OBS 26.1.1 (64-bit, windows) - Profile: Stream2k21 - Scenes: Scene')[0]
OBS.activate()
keyboard.send('win+shift+l')
time.sleep(0.01)
active.activate()

