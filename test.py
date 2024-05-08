import pyautogui,sys,keyboard


# while True:
#     if keyboard.read_key('q'):
#         sys.exit()
#     else:
#         pyautogui.click(291,386)

while True:
    pyautogui.click(291,386)
    if not keyboard.read_key('q'):
        break