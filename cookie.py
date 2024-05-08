import pyautogui,sys,keyboard


# while True:
#     if keyboard.read_key('q'):
#         sys.exit()
#     else:
#         pyautogui.click(291,386)

for i in range(50):
    if keyboard.read_key('q'):
        sys.exit()
    pyautogui.click(291,386)