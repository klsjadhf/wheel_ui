import tkinter as tk
from tkinter import ttk
import time
import threading

is_fullscreen = False

root = tk.Tk()
root.geometry("800x480")
root.configure(bg="blue")

s = ttk.Style()
s.configure("MyStyle.TFrame", background="black", border=0, relief="flat")
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

arc_line_width = 3
arc_line_colour = "white"
arc_fill_colour = "grey"
rect_line_colour = "white"
rect_fill_colour = "black"
text_unit_colour = "blue"
text_unit_font = ("Helvetica", 24)
s.configure("MyStyle.TLabel", relief="solid", background="black", foreground='white', anchor=tk.CENTER, font=('Helvetica', 24))

# N1
frame_N1 = ttk.Frame(dashboard, style="MyStyle.TFrame")
print("hi")
print(frame_N1.winfo_width())
frame_N1.grid(column=0, row=0, sticky="nsew")

canvas_N1 = tk.Canvas(frame_N1, bg="green", highlightthickness=0)
canvas_N1.pack(fill="both", expand=True)

arc_N1 = canvas_N1.create_arc(10, 0, 150, 140, outline=arc_fill_colour, fill=arc_fill_colour, width=arc_line_width, start=0, extent=-0)
canvas_N1.create_arc(10, 0, 150, 140, outline=arc_line_colour, width=arc_line_width, start=0, extent=-190, style="arc")

label_N1 = ttk.Label(canvas_N1, style="MyStyle.TLabel", text="error")
canvas_N1.create_window(100, 10, width=156, height=58, anchor='nw', window=label_N1)

canvas_N1.create_text(180, 100, text='N1 %', anchor='nw', font=text_unit_font, fill=text_unit_colour)


# FCT
frame_FCT = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_FCT.grid(column=0, row=1, sticky="nsew")

canvas_FCT = tk.Canvas(frame_FCT, bg="yellow", highlightthickness=0)
canvas_FCT.pack(fill="both", expand=True)


# PWR_FF
frame_PWR_FF = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_PWR_FF.grid(column=0, row=2, sticky="nsew")

canvas_FF = tk.Canvas(frame_PWR_FF, bg="red", highlightthickness=0)
canvas_FF.pack(fill="both", expand=True)


# SPD
frame_SPD = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_SPD.grid(column=1, row=0, sticky="nsew", rowspan=2, columnspan=2)

canvas_SPD = tk.Canvas(frame_SPD, bg="orange", highlightthickness=0)
canvas_SPD.pack(fill="both", expand=True)


# ST_FC
frame_ST_FC = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_ST_FC.grid(column=1, row=2, sticky="nsew")

canvas_ST_FC = tk.Canvas(frame_ST_FC, bg="lime", highlightthickness=0)
canvas_ST_FC.pack(fill="both", expand=True)


# FUEL
frame_FUEL = ttk.Frame(dashboard, style="MyHilight.TFrame")
frame_FUEL.grid(column=2, row=2, sticky="nsew")

canvas_FUEL = tk.Canvas(frame_FUEL, bg="purple", highlightthickness=0)
canvas_FUEL.pack(fill="both", expand=True)


def inc_pie():
    for i in range(190):
        canvas_N1.itemconfigure(arc_N1, extent=-i)
        time.sleep(0.01)
        label_N1["text"] = i/10
        # print("hi")
    input("end")

thread1 = threading.Thread(target=inc_pie, daemon=True)
thread1.start()

# keep the window displaying
root.mainloop()
