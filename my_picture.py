import colorsys
import random
import math
import tkinter as tk

# Internal state variables to track the "paintbrush"
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
    
    # Call the student's function, passing only the width and height
    draw_function(width, height)
    
    # Start the GUI loop
    root.mainloop()

# =====================================================================
# HELPER FUNCTIONS
# =====================================================================

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

# =====================================================================
# DRAWING API FOR STUDENTS
# =====================================================================

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
# CUSTOM LIGHTNING SHAPE FUNCTION (Matches Image Exactly)
# =====================================================================

def lightning(x, y, scale=0.4):
    """Draws a unified, custom vector lightning bolt matching your reference image.
    
    The scale parameter adjusts how big it prints (e.g., 0.4 means 40% size).
    """
    set_fill_color("#FFD200")     # Solid golden yellow
    set_outline_color("#FFA500")  # Orange borders
    set_line_thickness(3)
    
    # Precise 7-vertex path tracking the outer border coordinates of your picture
    points = [
        x + 55 * scale,  y + 0 * scale,    # 1. Top left corner
        x + 195 * scale, y + 0 * scale,    # 2. Top right corner
        x + 105 * scale, y + 105 * scale,  # 3. Inner right indentation
        x + 179 * scale, y + 105 * scale,  # 4. Right side middle shelf
        x + 20 * scale,  y + 295 * scale,  # 5. Sharp bottom tip
        x + 60 * scale,  y + 150 * scale,  # 6. Inner left indentation
        x + 5 * scale,   y + 150 * scale   # 7. Left side middle shelf
    ]
    
    _canvas.create_polygon(points, fill=_fill_color, outline=_outline_color, width=_line_thickness)


# =====================================================================
# MAIN PICTURE CREATION
# =====================================================================

def draw_picture(width, height):
    """Draws a static picture combining scenery elements, clouds, forest, and lightning."""
    
    # 1. Fill the background
    fill_background("white")
    
    # 2. Make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    triangle_height = height / 5
    triangle_width = width / 3
    
    # 3. Draw a red circle
    set_fill_color(colors[0])
    fill_circle(450, 50, 50)

    # 4. Draw the Mountain
    set_fill_color("#827e7e") # relatively dark gray
    fill_triangle(300, 150, 400, 20, 350, 150)
    set_fill_color("#c7c1c1") # lighter gray
    fill_triangle(350, 150, 400, 20, 550, 150)

    # 5. Draw Clouds (Behind trees, but overlapping sky/mountains)
    set_fill_color("white")
    set_outline_color("#cccccc")   # light-gray edge so clouds are visible
    set_line_thickness(1)

    # Cloud 1 — left side of sky
    fill_circle(80,  90, 30)
    fill_circle(110, 75, 38)
    fill_circle(145, 82, 28)
    fill_circle(170, 90, 22)

    # Cloud 2 — centre sky (small, fluffy)
    fill_circle(240, 55, 22)
    fill_circle(265, 43, 30)
    fill_circle(295, 50, 24)
    fill_circle(318, 58, 18)

    # 6. Draw Horizon
    set_outline_color("black")
    set_line_thickness(1)
    draw_line(0, 150, 600, 150)
    
    # 7. Draw River Curve
    river_points = [
        (100, 150), # Start point
        (300, 200), # Bends towards here
        (200, 350), # Bends back here
        (500, 500)  # End point
    ]
    set_outline_color("black")
    set_line_thickness(2)
    draw_curve(river_points)
    
    # 8. Draw Forest
    for x in range(40, 500, 70):
        # tree trunk
        set_fill_color("#F325FF")  # purple-pink brown 
        fill_rectangle(x, 110, 15, 40)
        
        # tree leaves
        set_fill_color("darkgreen")
        fill_triangle(x - 20, 119, x + 35, 120, x + 3, 70)
        fill_triangle(x - 15, 96, x + 30, 95, x + 7, 50)
    
    # 9. Draw the lightning strikes LAST (Keeps them on top layer over clouds/mountains)
    lightning(350, -10, scale=0.5)  # Larger strike piercing right over mountain peak
    lightning(80, 20, scale=0.35)   # Smaller strike on the left over the woods
    

if __name__ == "__main__":
    # Start the single combined canvas window
    start(draw_picture, 600, 400)
