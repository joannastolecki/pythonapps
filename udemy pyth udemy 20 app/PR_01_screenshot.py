# pip install pyautogui
#  pip install time

import time
import pyautogui as pg

# function create 
def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(5) # delay excecution
    img = pg.screenshot(name)
    img.show()
    
screenshot()

    
    
    