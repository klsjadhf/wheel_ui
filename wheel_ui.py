from re import S
import tkinter as tk
from tkinter import ttk
from turtle import bgcolor

is_fullscreen = False

root = tk.Tk()
root.minsize(600, 300)
root.configure(bg="blue")

s = ttk.Style()
s.configure("MyStyle.TFrame", background="black")
s.configure("MyHilight.TFrame", background="red")
s.configure("MyHilight.TLabel", background="red")

root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

def toggleFullscreen():
	global is_fullscreen
	if is_fullscreen:
		root.attributes('-fullscreen', False)
		is_fullscreen = False
	else:
		root.attributes('-fullscreen', True)
		is_fullscreen = True

startBtn = ttk.Button(root, text="toggle", command=toggleFullscreen)
startBtn.grid(column=0, row=0, sticky="ne")

dashboard = ttk.Frame(root, style="MyStyle.TFrame")
dashboard.grid(column=0, row=1, sticky="nsew")

# create 3x3 grid
for row in range (3):
    dashboard.rowconfigure(row, weight=1)
for col in range(3):
    dashboard.columnconfigure(col, weight=1)


frame_N1 = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_N1.grid(column=0, row=0, sticky="nsew")

# # place a label on the root window
message = ttk.Label(frame_N1, text="N1 placeholder")
message.pack()


frame_FCT = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_FCT.grid(column=0, row=1, sticky="nsew")

# # place a label on the root window
message = ttk.Label(frame_FCT, text="FCT placeholder")
message.pack()


frame_PWR_FF = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_PWR_FF.grid(column=0, row=2, sticky="nsew")

# # place a label on the root window
message = ttk.Label(frame_PWR_FF, text="PWR_FF placeholder")
message.pack()


frame_SPD = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_SPD.grid(column=1, row=0, sticky="nsew", rowspan=2, columnspan=2)

# # place a label on the root window
message = ttk.Label(frame_SPD, text="SPD placeholder")
message.pack()


frame_ST_FC = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_ST_FC.grid(column=1, row=2, sticky="nsew")

# # place a label on the root window
message = ttk.Label(frame_ST_FC, text="ST_FC placeholder")
message.pack()


frame_FUEL = ttk.Frame(dashboard, style="MyHilight.TFrame")
frame_FUEL.grid(column=2, row=2, sticky="nsew")

# # place a label on the root window
message = ttk.Label(frame_FUEL, text="FUEL placeholder")
message.pack()


# keep the window displaying
root.mainloop()
