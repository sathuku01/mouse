from pynput import mouse
import matplotlib.pyplot as plt
import time
import pyautogui
import randomwalk
import subprocess

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
        randomwalk.random_walk_to()
        pyautogui.click()
        print("Clicked mouse after moving")

        # Reset GNOME's idle timer - CORRECT SYNTAX
        subprocess.run([
            "dbus-send",
            "--session",
            "--type=method_call",
            "--dest=org.gnome.Mutter.IdleMonitor",
            "/org/gnome/Mutter/IdleMonitor/Core",
            "org.gnome.Mutter.IdleMonitor.Reset",
            "uint32:0"
        ], check=False, capture_output=True)
        listener.join()

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    plt.figure()
    plt.plot(x, y)
    plt.gca().invert_yaxis()  # Match screen coordinates
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Mouse Path")
    plt.show(block=False)
    plt.pause(2)       # keep window open for 2 seconds
    plt.close()

if __name__ == "__main__":
    execute()

