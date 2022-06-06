import tkinter as tk
from tkinter import ttk
import time
import threading
import math
import fuel_cell_comm as fcc

is_fullscreen = False

root = tk.Tk()
root.geometry("800x480")
root.configure(bg="black")

s = ttk.Style()
s.configure("MyStyle.TFrame", background="black", border=0)
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

startBtn = ttk.Button(root, text="FS", command=toggleFullscreen)
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

        #print(self.start_x, self.start_y, self.end_x, self.end_y)

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


text_label_font = ("Futura", 48)
text_status_font = ("Futura", 32)
text_label_color = "white"
arc_line_width = 3
arc_line_colour = "white"
arc_fill_colour = "grey"
rect_line_colour = "white"
rect_fill_colour = "black"
text_unit_colour = "blue"
text_unit_font = ("Helvetica", 22)
spdo_line_width = 5
spdo_line_colour = "white"
spdo_colour = "cyan"
circle_colour = "cyan"
circle_line_width = 3
s.configure("MyStyle.TLabel", relief="solid", background='black', foreground='white', anchor=tk.CENTER, font=('Helvetica', 24))
s.configure("Spdo.TLabel", background='black', foreground='white', anchor=tk.CENTER, font=('Helvetica', 40))
s.configure("MyStyle1.TLabel", relief="solid", background="black", anchor=tk.CENTER, font=('Helvetica', 20))
s.configure("Units.TLabel", background="black", foreground='blue', anchor=tk.CENTER, font=('Helvetica', 20))
# s.configure("MyStyle.TButton", background="black", foreground='blue', anchor=tk.CENTER, font=('Helvetica', 20))


######## N1 ########
frame_N1 = ttk.Frame(dashboard, style="MyStyle.TFrame")
print(frame_N1.winfo_width())
frame_N1.grid(column=0, row=0, sticky="nsew")
canvas_N1 = tk.Canvas(frame_N1, bg="black", highlightthickness=0)
canvas_N1.pack(fill="both", expand=True)

# Fill Arc
arc_N1 = canvas_N1.create_arc(10, 0, 150, 140, outline=arc_fill_colour, fill=arc_fill_colour, width=arc_line_width, start=0, extent=-0)
canvas_N1.create_arc(10, 0, 150, 140, outline=arc_line_colour, width=arc_line_width, start=0, extent=-190, style="arc")

# Box and value
canvas_N1.create_polygon(200, 5,  80, 5,  80, 70,  200, 70,  outline='gray', width='3')
label_N1 = canvas_N1.create_text(142, 37, width=200, text="N/A", anchor='center', font=text_status_font, fill=text_label_color)



canvas_N1.create_text(160, 80, text='N1 %', anchor='nw', font=text_unit_font, fill=text_unit_colour)


######## Fuel cell temperature ########
frame_FCT = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_FCT.grid(column=0, row=1, sticky="nsew")
canvas_FCT = tk.Canvas(frame_FCT, bg="black", highlightthickness=0)
canvas_FCT.pack(fill="both", expand=True)

# Fill Arc
arc_FCT = canvas_FCT.create_arc(10, 0, 150, 140, outline=arc_fill_colour, fill=arc_fill_colour, width=arc_line_width, start=0, extent=-0)
canvas_FCT.create_arc(10, 0, 150, 140, outline=arc_line_colour, width=arc_line_width, start=0, extent=-190, style="arc")

# Box and value
canvas_FCT.create_polygon(200, 5,  80, 5,  80, 70,  200, 70,  outline='gray', width='3')
label_FCT = canvas_FCT.create_text(142, 37, width=200, text="N/A", anchor='center', font=text_status_font, fill=text_label_color)

canvas_FCT.create_text(160, 80, text='FCT \N{DEGREE SIGN}C', anchor='nw', font=text_unit_font, fill=text_unit_colour)



######## Power and fuel flow ########
frame_PWR_FF = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_PWR_FF.grid(column=0, row=2, sticky="nsew")
canvas_PWR_FF = tk.Canvas(frame_PWR_FF, bg="black", highlightthickness=0)
canvas_PWR_FF.pack(fill="both", expand=True)

# create 2x2 grid
for row in range (2):
    frame_PWR_FF.rowconfigure(row, weight=1)
for col in range(2):
    frame_PWR_FF.columnconfigure(col, weight=1, minsize=130)


canvas_PWR_FF.create_polygon(130, 5,  10, 5,  10, 70,  130, 70,  outline='gray', width='3')
label_PWR = canvas_PWR_FF.create_text(72, 37, width=200, text="N/A", anchor='center', font=text_status_font, fill=text_label_color)
canvas_PWR_FF.create_text(145, 30, text='PWR x W', anchor='nw', font=text_unit_font, fill=text_unit_colour)

canvas_PWR_FF.create_polygon(130, 75,  10, 75,  10, 135,  130, 135,  outline='gray', width='3')
label_FF = canvas_PWR_FF.create_text(72, 107, width=200, text="N/A", anchor='center', font=text_status_font, fill=text_label_color)
canvas_PWR_FF.create_text(145, 100, text='FF / MIN', anchor='nw', font=text_unit_font, fill=text_unit_colour)



######## Speedometer ########
frame_SPD = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_SPD.grid(column=1, row=0, sticky="nsew", rowspan=2, columnspan=2)

canvas_SPD = tk.Canvas(frame_SPD, background="black", highlightthickness=0, selectbackground='black')
canvas_SPD.pack(fill="both", expand=True)

canvas_SPD.create_arc(10, 10, 520, 520, outline=spdo_colour, width=spdo_line_width, start=0, extent=180, style="arc")

for a in range(0,181,18):
    segment = RotatableLine(canvas_SPD, 265, 265, 255, 20, a)
    canvas_SPD.itemconfigure(segment.line, fill=spdo_colour, width=spdo_line_width)


needle = RotatableLine(canvas_SPD, 265, 265, 255, 50, 180)
canvas_SPD.itemconfigure(needle.line, fill=spdo_line_colour, width=spdo_line_width)

speed_reading = canvas_SPD.create_text(260, 100, width=400, text="NO DATA", anchor='n', font=text_label_font, fill=text_label_color)
canvas_SPD.create_text(200, 180, text='SPD X KM/H', anchor='nw', font=text_unit_font, fill=text_unit_colour)
status_message = canvas_SPD.create_text(260, 220, width=400, text="STATUS", anchor='n', font=text_status_font, fill=text_label_color)

def start_FC():
    fcc.start_fuel_cell()

def stop_FC():
    fcc.stop_fuel_cell()

######## Buttons ######## 
frame_ST_FC = ttk.Frame(dashboard, style="MyStyle.TFrame")
frame_ST_FC.grid(column=1, row=2, sticky="nsew")

canvas_ST_FC = tk.Canvas(frame_ST_FC, bg="black", highlightthickness=0)
canvas_ST_FC.pack(fill="both", expand=True)

# FC_button = ttk.Button(canvas_ST_FC, style="MyStyle.TButton", text="Start\nFC", command=start_FC)
frame_ST_FC.update()
ST_FC_width = frame_ST_FC.winfo_width()/ 1.483
ST_FC_height = frame_ST_FC.winfo_height() 

#circle_y1 = 5
#circle_rad = (ST_FC_height - (circle_y1*2))/2
#circle_x1 = (ST_FC_width/2) - circle_rad
#circle_y2 = circle_y1 + (2*circle_rad)
#circle_x2 = circle_x1 + (2*circle_rad)
#canvas_ST_FC.create_oval(circle_x1, circle_y1, circle_x2, circle_y2, outline=circle_colour, width=circle_line_width)

FC_Start_button = tk.Button(canvas_ST_FC, border=0, bg="black", fg="blue", font=('Futura', 24), text="START", command=start_FC)
FC_Stop_button = tk.Button(canvas_ST_FC, border=0, bg="black", fg="blue", font=('Futura', 24), text="STOP", command=stop_FC)
FC_Start_button.place(bordermode='inside', anchor='center', relx=0.45, rely=0.2, width=150, height=60)
FC_Stop_button.place(bordermode='inside', anchor='center', relx=0.45, rely=0.7, width=150, height=60)

#canvas_ST_FC.create_window(0, 0, width=ST_FC_width, height=ST_FC_height, anchor='nw', window=FC_button) 

# FUEL
frame_FUEL = ttk.Frame(dashboard, style="MyHilight.TFrame")
frame_FUEL.grid(column=2, row=2, sticky="nsew")
canvas_FUEL = tk.Canvas(frame_FUEL, bg="black", highlightthickness=0)
canvas_FUEL.pack(fill="both", expand=True)

canvas_FUEL.create_polygon(160, 45,  40, 45,  40, 110,  160, 110,  outline='blue', width='3')
label_FUEL = canvas_FUEL.create_text(102, 77, width=200, text="N/A", anchor='center', font=text_status_font, fill=text_label_color)
canvas_FUEL.create_text(110, 10, text='FUEL QTY x BAR', anchor='n', font=text_unit_font, fill=text_unit_colour)



def update_status(statusstring):
    canvas_SPD.itemconfigure(status_message, text=statusstring)

def update_FCT(value):
    canvas_FCT.itemconfigure(label_FCT, text = value)
    value_fraction = clamp(((value - 10) / 60.0), 0, 180)
    circle_progress = -value_fraction * 180
    canvas_FCT.itemconfigure(arc_FCT, extent=circle_progress)

def update_PWR(value):
    canvas_PWR_FF.itemconfigure(label_PWR, text = value)

def update_FF(value):
    canvas_PWR_FF.itemconfigure(label_FF, text = value)

def update_fuel(value):
    canvas_FUEL.itemconfigure(label_FUEL, text = value)


def main_ui_loop():
    pass

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))

def ui_cycle_test():
    for i in range(101):

        halfcircle_progress = (180*i)/100

        canvas_N1.itemconfigure(arc_N1, extent=-halfcircle_progress)  # extent is angle in degrees
        canvas_N1.itemconfigure(label_N1, text=i)
        
        canvas_FCT.itemconfigure(arc_FCT, extent=-halfcircle_progress) # extent is angle in degrees
        canvas_FCT.itemconfigure(label_FCT, text = i)

        needle.rotate_line(180-halfcircle_progress)
        canvas_SPD.itemconfigure(speed_reading, text=i)

        canvas_PWR_FF.itemconfigure(label_FF, text = i)
        canvas_PWR_FF.itemconfigure(label_PWR, text = i)

        canvas_FUEL.itemconfigure(label_FUEL, text = i)

        time.sleep(0.01)


def process_received_data(data):

    if ('FCT' in data):
        fct1 = fcc.extract_val("FCT1", data)
        fct2 = fcc.extract_val("FCT2", data)
        fcw = fcc.extract_val("FC_W", data)
        tank_p = fcc.extract_val("Tank-P", data)

        update_FCT(round((fct1 + fct2)/2,1))
        update_PWR(round(fcw,1))
        update_fuel(round(tank_p,1))

    elif ('ntu fc car' in data.lower()):
        update_status('CONNECTED')
        # Initial connection established

    elif ('of cells' in data.lower()):
        update_status('READY TO START')
        # Fuel cell ready with watchdog

    elif ('system off' in data.lower() or 'ready to start' in data.lower()):
        update_status('READY TO START')
        
        update_FCT(0)
        update_PWR(0)
        update_fuel(0)
        update_FF(0)
        # Fuel cell ready

    elif ('initiating' in data.lower()):
        update_status('STARTING FUEL CELL')
        update_FCT(0)
        update_PWR(0)
        update_fuel(0)
        update_FF(0)
        # Startup phase

    elif ('low h2 supply' in data.lower()):
        update_status('LOW H2 PRESSURE')
        # Awaiting H2

    elif ('over pressure' in data.lower()):
        update_status(data.upper())
        # over pressure

    elif ('shutdown initiated' in data.lower()):
        update_status('FUEL CELL SHUTDOWN')
        # fc shutting down

    elif ('OK' in data):
        update_status(data.upper())
        # miscellaneous status message (notify)

    elif ('entering to running' in data.lower()):
        update_status(' ')
        # clear status box here

    elif ('error' in data.lower() or 'compromised' in data.lower()):
        update_status(data.upper())
        # send warning message here

def fuel_cell_data_loop():
    while(True):
        time.sleep(0.5)

        fc_data = fcc.recv_fuel_cell()
        if len(fc_data) > 0:
            print(fc_data)
            process_received_data(fc_data.strip())



thread1 = threading.Thread(target=main_ui_loop, daemon=True)
thread1.start()

thread2 = threading.Thread(target=fuel_cell_data_loop, daemon=True)
thread2.start()

# keep the window displaying
root.mainloop()
