# pip install pyautogui
#  pip install time

import time
import pyautogui as pg
import tkinter as tk

# function create 
def screenshot():
    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(5) # delay excecution
    img = pg.screenshot(name)
    img.show()
    
#screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take screen shot",
    command=screenshot)
button.pack(side=tk.LEFT)


close = tk.Button(
    frame,
    text="Quit",
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
    
    
    