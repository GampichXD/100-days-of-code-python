# Professional Portfolio Project - GUI Automation
# Automate the Google Dinosaur Game
# Author : Abraham
import time
import random
import keyboard
import pyautogui
from PIL import ImageGrab
import win32api, win32con

time.sleep(2)
jump_count = 0

# Key press functions
def press_key(key):
    win32api.keybd_event(key, 0, 0, 0)
    time.sleep(0.01)
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

def jump():
    global jump_count
    press_key(38)  # Up arrow
    jump_count += 1
    print(f"[Jump] Total: {jump_count}")

def duck():
    press_key(40)  # Down arrow
    time.sleep(0.25)
    print("[Duck] Detected flying obstacle")

# Regions or pixel positions to detect obstacles
pixels = {
    "short_cactus": (710, 490),
    "tall_cactus": (730, 470),
    "pterodactyl": (755, 455)
}

def obstacle_detected(pos, threshold=90):
    r, g, b = pyautogui.pixel(pos[0], pos[1])
    return r < threshold and g < threshold and b < threshold

print("Bot started. Press 'q' to quit...")

# Main loop
while not keyboard.is_pressed('q'):
    time.sleep(random.uniform(0.01, 0.03))  # Random delay to simulate reaction time

    if obstacle_detected(pixels["short_cactus"]):
        jump()
        print("Short cactus detected.")

    elif obstacle_detected(pixels["tall_cactus"]):
        jump()
        print("Tall cactus detected.")

    elif obstacle_detected(pixels["pterodactyl"]):
        duck()

    # Optional: add dynamic difficulty handling here


if __name__ == "__main__":
    main()




     
