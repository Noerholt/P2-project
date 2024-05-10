import tkinter as tk
from pymycobot.mycobot import MyCobot
from pymycobot import PI_PORT, PI_BAUD
from kinematicsLibrary import *

mc = MyCobot("COM5", 115200)
mc.set_world_reference([0,0,0,0,0,0])
mc.sync_send_angles([0,0,0,0,0,0],25)
C = mc.get_coords()
x0, y0 = 0
mode = True # True = Position & False = Orientation 

def on_mouse_scroll(event):
    if event.delta > 0: #Scrolled up
        if(mode):
            C[2] += 1
        else:
            C[5] += 0.5
    else: #Scrolled down
        if(mode):
            C[2] -= 1
        else:
            C[5] -= 0.5
    mc.send_coords(C, 25, 0)

def on_mouse_move(event):
    if (event.x > x0):
        if(mode):
            C[0] += 1
        else:
            C[3] += 0.5
    else:
        if(mode):
            C[0] -= 1
        else:
            C[3] -= 0.5
    x0 = event.x
    if (event.y > y0):
        if(mode):
            C[1] += 1
        else:
            C[4] += 0.5
    else:
        if(mode):
            C[1] -= 1
        else:
            C[4] -= 0.5
    y0 = event.y
    mc.send_coords(C, 25, 0)
    
def on_space_key(event):
    mode = not mode

def on_enter_key(event):
    root.quit()

root = tk.Tk()
root.title("Robot Motion")
root.bind('<Motion>', on_mouse_move)
root.bind("<MouseWheel>", on_mouse_scroll)
root.bind("<space>", on_space_key)
root.bind("<Return>", on_enter_key)

root.mainloop()