import pyautogui
import time

# Optional safety: move mouse to a screen corner to abort
pyautogui.FAILSAFE = True

INTERVAL = 15  # seconds between clicks

print("Auto-clicker started. Press Ctrl+C to stop.")
print("(Move mouse to a screen corner to trigger the emergency failsafe.)")

try:
    while True:
        pyautogui.click()
        print(f"Clicked at {time.strftime('%H:%M:%S')}")
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    print("\nAuto-clicker stopped.")