
import pyautogui

import os

from time import sleep

script_dir = os.path.dirname(os.path.realpath(__file__))

capslock_command = script_dir + '/CheckModKeys capslock'

is_capslock_set = lambda: bool(int(os.popen(capslock_command).read().strip()))

delay = 0

while True:
  if is_capslock_set():
    pyautogui.click(*pyautogui.position())
    if delay > 0: sleep(delay)
  else:
    sleep(0.1)


