import pyautogui
import sys
import keyboard


while True:
    if keyboard.is_pressed('q'):
        break
    else:
        pyautogui.click(291,386)

# for i in range(50):
#     if keyboard.read_key('q'):
#         sys.exit()
#     pyautogui.click(291,386)


# for i in range(1000):
#     pyautogui.click(291,386)


# try:
#     while True:
#         pyautogui.click(291,386)
# except KeyboardInterrupt:
#     print('Stop')