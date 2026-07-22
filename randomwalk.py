import math
import random
import time
import pyautogui



def random_walk_to():

    width, height = pyautogui.size()
    widthto, heightto = width * .6, height/height
   
    print(f"Screen width: {width}")
    print(f"Screen height: {height}")
   
    x, y = pyautogui.position()

    max_step = 25
    min_step = 3

    max_noise = 0.5   # radians (~29 degrees)
    min_noise = 0.05  # radians (~3 degrees)

    while True:
        dx = widthto - x
        dy = heightto - y

        distance = math.hypot(dx, dy)

        # Stop when close enough
        if distance < 3:
            pyautogui.moveTo(widthto, heightto)
            break

        # Normalize distance (0 -> 1)
        factor = min(distance / max(width, height), 1)

        # Adaptive step size
        step = min_step + (max_step - min_step) * factor

        # Adaptive randomness
        noise = min_noise + (max_noise - min_noise) * factor

        # Direction to target
        angle = math.atan2(dy, dx)

        # Add random deviation
        angle += random.gauss(0, noise)

        # Take a step
        x += step * math.cos(angle)
        y += step * math.sin(angle)

        # Keep inside screen
        x = max(0, min(width - 1, x))
        y = max(0, min(height - 1, y))

        pyautogui.moveTo(
            round(x),
            round(y),
            duration=random.uniform(0.05, 0.15)
        )

        # Small timing variation
        time.sleep(random.uniform(0.02, 0.08))


if __name__ == "__main__":
    random_walk_to()