import pyautogui

def rand():
    width, height = pyautogui.size()
    # bear.execute()
    print(f"Screen width: {width}")
    print(f"Screen height: {height}")
    pyautogui.moveTo(
        width * .6,
        height/height,
        duration=1
    )

if __name__ == "__main__":
    rand()