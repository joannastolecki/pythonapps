# pip install pyautogui
#  pip install time

import time
import pyautogui as pg
import tkinter as tk

# function create 
def test():
    print("aska")
    
#screenshot()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take screen shot",
    command=test)    # wywolanie funkcji
button.pack(side=tk.LEFT)


close = tk.Button(
    frame,
    text="Quit",
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
    
    
    