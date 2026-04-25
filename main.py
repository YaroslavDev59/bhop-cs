import keyboard
import time
import random

def run_bhop():
    activation_key = 'caps lock'
    print("Script runned , hold CAPS LOCK")

    while True:
        if keyboard.is_pressed(activation_key):
            keyboard.press_and_release('space')
            time.sleep(0.02)
        else:
            time.sleep(0.01)    

if __name__ == "__main__":
    run_bhop()
