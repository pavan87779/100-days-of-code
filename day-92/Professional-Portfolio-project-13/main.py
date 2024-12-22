import time
from PIL import ImageGrab
import keyboard  # Alternative to pyautogui for key presses

# Dynamically get the obstacle detection area
X, Y = 500, 500  # Adjust manually based on game window position
WIDTH, HEIGHT = 60, 40  # Adjust based on game size

def is_obstacle_present():
    try:
        print("Taking screenshot...")
        # Take a screenshot of the game area
        screenshot = ImageGrab.grab(bbox=(X, Y, X + WIDTH, Y + HEIGHT))
        print("Screenshot taken.")
        pixels = screenshot.load()

        # Check for dark pixels indicating obstacles
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if pixels[x, y][0] < 100:  # Detect dark objects (obstacles)
                    return True
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False

def jump():
    print("Jumping...")
    keyboard.press_and_release('space')

if __name__ == "__main__":
    try:
        print("Starting in 3 seconds... Move to game window")
        time.sleep(3)

        while True:
            if is_obstacle_present():
                jump()

            time.sleep(0.05)

    except KeyboardInterrupt:
        print("Program interrupted. Exiting...")

