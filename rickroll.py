import keyboard
import pyautogui



while True: 
        if keyboard.is_pressed('f'):
            print(pyautogui.position())
            keyboard.press_and_release('left windows+r')
            pyautogui.click(294,975)
            keyboard.press_and_release('ctrl+a')
            pyautogui.write("https://youtu.be/dQw4w9WgXcQ")
            pyautogui.click(190,1041)
            
            
            