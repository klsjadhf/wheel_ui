import tkinter as tk
from tkinter import ttk
import time
import threading
import math

is_fullscreen = False

root = tk.Tk()
root.geometry("800x480")
root.configure(bg="black")

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

# def rotate_line(parent_canvas, line, angle):
#     angle = -math.radians(angle)
#     end_x = mid_pt_x + (radius * math.cos(angle))
#     end_y = mid_pt_y + (radius * math.sin(angle))
#     start_x = end_x - (len * math.cos(angle))
#     start_y = end_y - (len * math.sin(angle))

#     print(start_x, start_y, end_x, end_y)
#     print(parent_canvas.coords(line))

#     parent_canvas.coords(line, start_x, start_y, end_x, end_y)
class RotatableLine:
    # parent canvas, mid points of circle, radius of circle, length from circumfrence to center, angle in degs
    def __init__(self, parent, mid_pt_x, mid_pt_y, radius, len, angle):
        self.parent = parent
        self.mid_pt_x = mid_pt_x
        self.mid_pt_y = mid_pt_y
        self.radius = radius
        self.len = len
        self.angle = -math.radians(angle)

        self.calculate_line()

    def calculate_line(self):
        self.end_x = self.mid_pt_x + (self.radius * math.cos(self.angle))
        self.end_y = self.mid_pt_y + (self.radius * math.sin(self.angle))
        self.start_x = self.end_x - (self.len * math.cos(self.angle))
        self.start_y = self.end_y - (self.len * math.sin(self.angle))

        print(self.start_x, self.start_y, self.end_x, self.end_y)

        self.line = self.parent.create_line(self.start_x, self.start_y, self.end_x, self.end_y)
    
    def rotate_line(self, angle):
        self.angle = -math.radians(angle)
        self.end_x = self.mid_pt_x + (self.radius * math.cos(self.angle))
        self.end_y = self.mid_pt_y + (self.radius * math.sin(self.angle))
        self.start_x = self.end_x - (self.len * math.cos(self.angle))
        self.start_y = self.end_y - (self.len * math.sin(self.angle))

        # print(start_x, start_y, end_x, end_y)
        # print(parent_canvas.coords(line))

        self.parent.coords(self.line, self.start_x, self.start_y, self.end_x, self.end_y)
    
# # parent canvas, mid points of circle, radius of circle, length from circumfrence to center, angle in degs
# def create_arc_seg(parent, mid_pt_x, mid_pt_y, radius, len, angle):
#     angle = -math.radians(angle)
#     end_x = mid_pt_x + (radius * math.cos(angle))
#     end_y = mid_pt_y + (radius * math.sin(angle))
#     start_x = end_x - (len * math.cos(angle))
#     start_y = end_y - (len * math.sin(angle))

#     print(start_x, start_y, end_x, end_y)

#     return parent.create_line(start_x, start_y, end_x, end_y)

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
spdo_line_width = 5
spdo_line_colour = "white"
spdo_colour = "cyan"
s.configure("MyStyle.TLabel", relief="solid", background="black", foreground='white', anchor=tk.CENTER, font=('Helvetica', 24))
s.configure("Spdo.TLabel", background="black", foreground='white', anchor=tk.CENTER, font=('Helvetica', 40))


# N1
frame_N1 = ttk.Frame(dashboard, style="MyStyle.TFrame")
print("hi")
print(frame_N1.winfo_width())
frame_N1.grid(column=0, row=0, sticky="nsew")

canvas_N1 = tk.Canvas(frame_N1, bg="black", highlightthickness=0)
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

canvas_SPD = tk.Canvas(frame_SPD, bg="black", highlightthickness=0)
canvas_SPD.pack(fill="both", expand=True)

canvas_SPD.create_arc(10, 10, 520, 520, outline=spdo_colour, width=spdo_line_width, start=0, extent=180, style="arc")
# test_line = canvas_SPD.create_line(250, 260, 300, 260)
# canvas_SPD.itemconfigure(test_line, fill=spdo_colour, width=spdo_line_width)

for a in range(0,181,18):
    segment = RotatableLine(canvas_SPD, 265, 265, 255, 20, a)
    canvas_SPD.itemconfigure(segment.line, fill=spdo_colour, width=spdo_line_width)

# seg_1 = create_arc_seg(canvas_SPD, 265, 265, 255, 200, 15)
needle = RotatableLine(canvas_SPD, 265, 265, 255, 50, 180)
canvas_SPD.itemconfigure(needle.line, fill=spdo_line_colour, width=spdo_line_width)

speed_reading = ttk.Label(canvas_SPD, style="Spdo.TLabel", text="error")
canvas_SPD.create_window(160, 120, width=200, height=80, anchor='nw', window=speed_reading)
canvas_SPD.create_text(160, 200, text='SPD X KM/H', anchor='nw', font=text_unit_font, fill=text_unit_colour)



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
    while (1):
        for i in range(190):
            canvas_N1.itemconfigure(arc_N1, extent=-i)
            time.sleep(0.01)
            label_N1["text"] = i/10
            # print("hi")
        print("loop")
        # rotate_line (canvas_SPD, seg_1,0)
        for i in range(180,0,-1):
            needle.rotate_line(i)
            speed_reading["text"] = i/10
            time.sleep(0.01)
        print("loop1")

thread1 = threading.Thread(target=inc_pie, daemon=True)
thread1.start()

# keep the window displaying
root.mainloop()
