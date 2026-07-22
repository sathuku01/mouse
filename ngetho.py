import ctypes
import time
import pyautogui
import subprocess

import bear


# Target coordinates
TARGET_X = 800
TARGET_Y = 400

# Idle threshold (3 minutes)
IDLE_SECONDS = 180
triggered = False

def get_idle_time():
    # xprintidle returns idle time in milliseconds
    idle_ms = subprocess.check_output(["xprintidle"])
    return int(idle_ms) / 1000

while True:
    idle = get_idle_time()

    if idle >= IDLE_SECONDS and not triggered:
        # pyautogui.moveTo(TARGET_X, TARGET_Y, duration=1)

        print("Moved mouse after 3 minutes idle.")
        triggered = True

    elif idle < IDLE_SECONDS:
        # User has interacted again
        triggered = False

    time.sleep(1)
