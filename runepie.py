import pyautogui
import time

coordinates = [(1241, 154), (1287, 150), (1736, 811), (1820, 912), (1457, 534), (1737, 806)]

time.sleep(3)

while True:
    for i, (x, y) in enumerate(coordinates):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        if i == 1:
            time.sleep(1)
            pyautogui.press('esc')
        if i == 2:
            continue
        elif i == 3:
            time.sleep(1)
            pyautogui.press('space')
            time.sleep(18)
        else:
           time.sleep(1)
