import math
import random
import time
import pyautogui


def random_walk_to():

    width, height = pyautogui.size()

    # Target location
    widthto, heightto = width * .6, height * .5

    print(f"Screen width: {width}")
    print(f"Screen height: {height}")

    x, y = pyautogui.position()

    # Brownian motion settings
    max_step = 15
    min_step = 2

    max_noise = 8
    min_noise = 1

    # Velocity for smoother Brownian movement
    vx, vy = 0, 0

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

        # Adaptive attraction strength
        step = min_step + (max_step - min_step) * factor

        # Adaptive Brownian noise
        noise = min_noise + (max_noise - min_noise) * factor

        # Direction toward target
        direction_x = dx / distance
        direction_y = dy / distance

        # Attraction force
        drift_x = direction_x * step
        drift_y = direction_y * step

        # Brownian random movement
        brownian_x = random.gauss(0, noise)
        brownian_y = random.gauss(0, noise)

        # Add forces to velocity
        vx += drift_x + brownian_x
        vy += drift_y + brownian_y

        # Damping to prevent runaway speed
        vx *= 0.75
        vy *= 0.75

        # Update position
        x += vx
        y += vy

        # Keep inside screen boundaries
        x = max(0, min(width - 1, x))
        y = max(0, min(height - 1, y))

        pyautogui.moveTo(
            round(x),
            round(y),
            duration=random.uniform(0.05, 0.15)
        )

        # Timing variation
        time.sleep(random.uniform(0.02, 0.08))


if __name__ == "__main__":
    random_walk_to()