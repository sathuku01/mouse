from pynput import mouse
import matplotlib.pyplot as plt
import time
import pyautogui
import randomwalk

def execute():
    points = []

    def on_move(x, y):
        points.append((x, y))

    def on_click(x, y, button, pressed):
        if not pressed:
            return False  # Stop recording when a mouse button is released

    with mouse.Listener(
        on_move=on_move,  
        on_click=on_click
    ) as listener:
        randomwalk.rand()
        time.sleep(3)
        pyautogui.click()
        print("Move the mouse. Click to stop.")
        listener.join()

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.plot(x, y)
    plt.gca().invert_yaxis()  # Match screen coordinates
    plt.xlabel("X") # x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.plot(x, y)
    plt.gca().invert_yaxis()  # Match screen coordinates
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Mouse Path")
    plt.show()

    plt.ylabel("Y")
    plt.title("Mouse Path")
    plt.show()

execute()

