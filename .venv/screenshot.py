# pip install pyautogui
#  pip install time

import time
import pyautogui

# function create 
def screenshot():
    name = int(round(time.time() * 1000))
    print(name)
    name = '/Users/iaska/github clones/pythonapps/.venv/{}.png'.format(name)
    print(name)
    time.sleep(5) # delay excecution
    img = pyautogui.screenshot(name)
    img.show()
    
    
screenshot()
    
    
    