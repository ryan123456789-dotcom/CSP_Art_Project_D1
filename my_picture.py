import colorsys
import random
import math
import tkinter as tk

_canvas = None
_fill_color = "black"
_outline_color = "black"
_line_thickness = 1

def start(draw_function, width=800, height=600):
    """Sets up the window and calls the student's drawing function."""
    global _canvas
    
    root = tk.Tk()
    root.title("Simple Graphics")
    root.resizable(False, False)
    
    # Create the drawing canvas
    _canvas = tk.Canvas(root, width=width, height=height, bg="white", highlightthickness=0)
    _canvas.pack()
    
    draw_function(width, height)
    
    root.mainloop()


def map_value(value, start1, stop1, start2, stop2):
    """Re-maps a number from one range to another."""
    percentage = (value - start1) / (stop1 - start1)
    return start2 + percentage * (stop2 - start2)


def hls_to_rgb_hex(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r_int = int(r * 255)
    g_int = int(g * 255)
    b_int = int(b * 255)
    return f"#{r_int:02x}{g_int:02x}{b_int:02x}"


def rgb_hex_to_hls(hex_str):
    hex_str = hex_str.lstrip('#')
    r, g, b = tuple(int(hex_str[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    return colorsys.rgb_to_hls(r, g, b)


def set_fill_color(color_name):
    global _fill_color
    _fill_color = color_name
    
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"    

def set_outline_color(color_name):
    global _outline_color
    _outline_color = color_name

def set_line_thickness(thickness):
    global _line_thickness
    _line_thickness = thickness

def fill_background(color_name):
    w = int(_canvas['width'])
    h = int(_canvas['height'])
    _canvas.create_rectangle(0, 0, w, h, fill=color_name, outline="")

def draw_line(x1, y1, x2, y2):
    _canvas.create_line(x1, y1, x2, y2, fill=_outline_color, width=_line_thickness)

def fill_rectangle(x, y, width, height):
    _canvas.create_rectangle(x, y, x + width, y + height, 
                             fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_rectangle(x, y, width, height):
    _canvas.create_rectangle(x, y, x + width, y + height, 
                             fill="", outline=_outline_color, width=_line_thickness)

def fill_circle(center_x, center_y, radius):
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_circle(center_x, center_y, radius):
    _canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, 
                        fill="", outline=_outline_color, width=_line_thickness)
    
def fill_triangle(x1, y1, x2, y2, x3, y3):
    _canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                           fill=_fill_color, outline=_outline_color, width=_line_thickness)

def draw_triangle(x1, y1, x2, y2, x3, y3):
    _canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                           fill="", outline=_outline_color, width=_line_thickness)
    
def fill_arc(x, y, width, height, start_angle, extent_angle):
    _canvas.create_arc(x, y, x + width, y + height, 
                       start=start_angle, extent=extent_angle, 
                       fill=_fill_color, outline=_outline_color, width=_line_thickness)
    
def draw_curve(points_list):
    if len(points_list) < 2:
        print("Error: A curve needs at least 2 points.")
        return
    flat_coordinates = []
    for x, y in points_list:
        flat_coordinates.append(x)
        flat_coordinates.append(y)
    _canvas.create_line(*flat_coordinates, smooth=True, fill=_outline_color, width=_line_thickness)
    

def draw_text(x, y, text_string, font_size=16):
    _canvas.create_text(x, y, text=text_string, fill=_fill_color, anchor="nw", font=("Arial", font_size))


# =====================================================================
# UPDATED MOUNTAIN FUNCTION WITH SNOW CAPS
# =====================================================================
def draw_mountain(peak_x, peak_y, base_width, base_y, color_hex):
    """Draws a mountain and adds a clean, proportional white snow cap to the peak."""
    # 1. Draw the main mountain body
    set_fill_color(color_hex)
    set_outline_color("grey")
    set_line_thickness(1)
    half_width = base_width / 2
    fill_triangle(peak_x - half_width, base_y, peak_x, peak_y, peak_x + half_width, base_y)
    
    # 2. Draw the snow cap (Top 25% of the mountain)
    snow_height_ratio = 0.25
    mountain_height = base_y - peak_y
    
    snow_base_y = peak_y + (mountain_height * snow_height_ratio)
    snow_half_width = half_width * snow_height_ratio
    
    set_fill_color("white")
    set_outline_color("#cccccc") # Light grey outline to make the white pop against the sky
    fill_triangle(peak_x - snow_half_width, snow_base_y, peak_x, peak_y, peak_x + snow_half_width, snow_base_y)


def lightning(x, y, scale=0.4):
    """Draws a unified, custom vector lightning bolt matching your reference image."""
    set_fill_color("#FFD200")     # Solid golden yellow
    set_outline_color("#FFA500")  # Orange borders
    set_line_thickness(3)
    
    points = [
        x + 55 * scale,  y + 0 * scale,    
        x + 195 * scale, y + 0 * scale,    
        x + 105 * scale, y + 105 * scale,  
        x + 179 * scale, y + 105 * scale,  
        x + 20 * scale,  y + 295 * scale,  
        x + 60 * scale,  y + 150 * scale,  
        x + 5 * scale,   y + 150 * scale   
    ]
    
    _canvas.create_polygon(points, fill=_fill_color, outline=_outline_color, width=_line_thickness)


# =====================================================================
# MAIN PICTURE
# =====================================================================
def draw_picture(width, height):
    """Draws a static picture combining scenery elements, clouds, forest, and lightning."""
    
    # 1. Fill the background sky
    fill_background("#FF8C00") 
    
    # 2. Draw a red circle
    set_fill_color("red")
    set_outline_color("black")
    set_line_thickness(1)
    fill_circle(450, 120, 50) 

    # 3. Draw Mountains (They will automatically render with snow caps now)
    # --- LEFT SIDE RANGE ---
    draw_mountain(150, 100, 200, 250, "#a0a0a0") 
    draw_mountain(250, 150, 250, 250, "#c0c0c0") 
    draw_mountain(100, 150, 300, 250, "#808080") 
    draw_mountain(220, 80, 250, 250, "#a0a0a0")  
    
    # --- RIGHT SIDE RANGE (Mirrored/Duplicated) ---
    draw_mountain(450, 100, 200, 250, "#a0a0a0") 
    draw_mountain(350, 150, 250, 250, "#c0c0c0") 
    draw_mountain(500, 150, 300, 250, "#808080") 
    draw_mountain(380, 80, 250, 250, "#a0a0a0")  

    # 4. Draw Lightning (Drawn behind the clouds)
    lightning(95, 50, scale=0.3)    
    lightning(390, 48, scale=0.22)
    
    # 5. Draw Clouds (Drawn on top of the lightning so it hides the flat top edge)
    set_fill_color("white")
    set_outline_color("#cccccc")   
    set_line_thickness(1)

    # Cloud 1 — Left side cluster
    fill_circle(80,  65, 30)
    fill_circle(110, 50, 38)
    fill_circle(145, 57, 28)
    fill_circle(170, 65, 22)

    # Cloud 2 — Right side cluster
    fill_circle(380, 55, 22)
    fill_circle(405, 43, 30)
    fill_circle(435, 50, 24)
    fill_circle(458, 58, 18)

    # 6. Fill the ground base
    set_fill_color("#41980a") 
    set_outline_color("")
    fill_rectangle(0, 250, 600, 150)

    # 7. Draw Horizon Line matching the bottom base of the mountains
    set_outline_color("black")
    set_line_thickness(1)
    draw_line(0, 250, 600, 250)
    
    # 8. Draw Forest (Way down in the absolute foreground)
    for x in range(30, 550, 85):
        set_fill_color("brown")  
        fill_rectangle(x, 260, 20, 60)
        
        set_fill_color("#0B6623")
        set_outline_color("black")
        fill_triangle(x - 30, 275, x + 50, 275, x + 10, 200)
        fill_triangle(x - 22, 240, x + 42, 240, x + 10, 170)


if __name__ == "__main__":
    # Start the single combined canvas window
    start(draw_picture, 600, 400)
