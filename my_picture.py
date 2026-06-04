import colorsys
import random
import math
import tkinter as tk

 def draw_meteor(x, y, size):

    # Outer glow
    set_fill_color("#FFD700")
    set_outline_color("")

    fill_circle(x - size*5, y - size*4, size)
    fill_circle(x - size*4, y - size*3, size)
    fill_circle(x - size*3, y - size*2, size)

    # Orange flame
    set_fill_color("#FFA500")

    fill_circle(x - size*4, y - size*3, size-2)
    fill_circle(x - size*3, y - size*2, size-2)
    fill_circle(x - size*2, y - size, size-2)

    # Red-hot core
    set_fill_color("#FF4500")

    fill_circle(x - size*3, y - size*2, size-4)
    fill_circle(x - size*2, y - size, size-4)

    # Meteor body
    set_fill_color("#5B4B43")
    set_outline_color("black")
    set_line_thickness(2)

    _canvas.create_polygon(
        x, y,
        x + size, y - size,
        x + size*2, y,
        x + size*1.7, y + size,
        x + size//2, y + size,
        x - size//2, y + size//3,
        fill=_fill_color,
        outline=_outline_color,
        width=2
    )

    # Craters
    set_fill_color("#2E2520")
    fill_circle(x + size//2, y, max(2, size//5))
    fill_circle(x + size, y + size//3, max(2, size//6))
    fill_circle(x + size//3, y + size//2, max(2, size//7))
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



#Written by James
def draw_mountain(peak_x, peak_y, base_width, base_y, color_hex):

    # 1. Draw the main mountain body
    set_fill_color(color_hex)
    set_outline_color("grey")
    set_line_thickness(1)
    half_width = base_width / 2
    fill_triangle(peak_x - half_width, base_y, peak_x, peak_y, peak_x + half_width, base_y)
    

    snow_height_ratio = 0.25
    mountain_height = base_y - peak_y
    
    snow_base_y = peak_y + (mountain_height * snow_height_ratio)
    snow_half_width = half_width * snow_height_ratio
    
    set_fill_color("white")
    set_outline_color("#cccccc") # Light grey outline to make the white pop against the sky
    fill_triangle(peak_x - snow_half_width, snow_base_y, peak_x, peak_y, peak_x + snow_half_width, snow_base_y)

#Written by Ryan with some AI to help tidy things up
def lightning(x, y, scale=0.4):
   
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

#Rain
#Written by Ryan with some AI to help tidy things up
def draw_rain(num_drops=150, max_y=250):
  
    set_outline_color("#6c8094")  
    set_line_thickness(2)
    
    for i in range(num_drops):
      
        x1 = random.randint(-20, 600)
        y1 = random.randint(0, max_y)
        
    
        length = random.randint(12, 22)
        slant = random.randint(3, 6)   
        
        x2 = x1 + slant
        y2 = y1 + length
        
  
        if y2 < max_y:
            draw_line(x1, y1, x2, y2)


def draw_chicken(x, y, scale, fill_color):
    """
    Draws a customizable chicken at a given center location and scale.
    
    AI Attribution:
    Generated by: Gemini
    Prompt: [Student: Place your exact prompt here, e.g., "I want to draw a chicken and be able to set all the parameters like x, y, scale, and also fill in the color"]
    """
    global _outline_color, _line_thickness
    
    # 1. Draw the legs (lines drawn behind the body)
    _canvas.create_line(x - 10 * scale, y + 20 * scale, x - 15 * scale, y + 45 * scale, fill=_outline_color, width=_line_thickness)
    _canvas.create_line(x + 10 * scale, y + 20 * scale, x + 15 * scale, y + 45 * scale, fill=_outline_color, width=_line_thickness)
    
    # 2. Draw the body (a wide oval)
    _canvas.create_oval(
        x - 30 * scale, y - 25 * scale, 
        x + 30 * scale, y + 25 * scale, 
        fill=fill_color, outline=_outline_color, width=_line_thickness
    )
    
    # 3. Draw the head (a smaller circle placed on the top right)
    _canvas.create_oval(
        x + 10 * scale, y - 45 * scale, 
        x + 40 * scale, y - 15 * scale, 
        fill=fill_color, outline=_outline_color, width=_line_thickness
    )
    
    # 4. Draw the beak (an orange triangle pointing right)
    _canvas.create_polygon(
        x + 38 * scale, y - 35 * scale, 
        x + 55 * scale, y - 30 * scale, 
        x + 38 * scale, y - 25 * scale, 
        fill="orange", outline=_outline_color, width=_line_thickness
    )
    
    # 5. Draw the eye (a small black dot)
    _canvas.create_oval(
        x + 25 * scale, y - 37 * scale, 
        x + 30 * scale, y - 32 * scale, 
        fill="black"
    )



def draw_trex(x, y, size, color, facing_direction):
    """
    Draws a detailed stylized T-Rex shape with an eye and teeth.
    
    AI Attribution:
    Generated by: Gemini
    Prompt: "yes [Keep parameters: x, y, size, color, facing_direction. Add a face, eye, and little bit more detail]"
    """
    global _canvas
    
    # Determine which way the T-Rex is facing
    direction_multiplier = 1
    if facing_direction.lower() == "left":
        direction_multiplier = -1
        
    # Helper function to easily scale and flip coordinate points
    def transform_points(points):
        transformed = []
        for px, py in points:
            transformed.append(x + (px * size * direction_multiplier))
            transformed.append(y + (py * size))
        return transformed

    # 1. Draw the main body
    base_points = [
        (40, -40), (10, -40), (10, -20), (-10, -10), 
        (-40, 10), (-40, 20), (-20, 10), (-10, 30), 
        (0, 30), (-5, 10), (5, 10), (10, 30), 
        (20, 30), (15, 10), (30, 5), (30, 10), 
        (20, 5), (20, -20), (40, -20)
    ]
    _canvas.create_polygon(*transform_points(base_points), fill=color, outline="black", width=2)
    
    # 2. Draw sharp teeth along the jawline
    teeth_points = [(35, -20), (32, -15), (29, -20), (26, -15), (23, -20)]
    _canvas.create_polygon(*transform_points(teeth_points), fill="white", outline="black", width=1)
    
    # 3. Draw the white part of the eye
    eye_x = x + (25 * size * direction_multiplier)
    eye_y = y + (-31 * size)
    eye_radius = 2.5 * size
    _canvas.create_oval(eye_x - eye_radius, eye_y - eye_radius, 
                        eye_x + eye_radius, eye_y + eye_radius, 
                        fill="white", outline="black", width=1)
    
    # 4. Draw the black pupil (looking slightly forward)
    pupil_x = x + (26 * size * direction_multiplier) 
    pupil_y = y + (-31 * size)
    pupil_radius = 1 * size
    _canvas.create_oval(pupil_x - pupil_radius, pupil_y - pupil_radius, 
                        pupil_x + pupil_radius, pupil_y + pupil_radius, 
                        fill="black", outline="")
    


def draw_picture(width, height):
  
    
    # 1. Fill the background sky
    fill_background("#FF8C00") 
    
    # 2. Draw the sun
    set_fill_color("red")
    set_outline_color("black")
    set_line_thickness(1)
    fill_circle(450, 120, 50) 

    # 3. Draw Mountains 
    #Written by James with some AI to help tidy things up

    draw_mountain(150, 100, 200, 250, "#a0a0a0") 
    draw_mountain(250, 150, 250, 250, "#c0c0c0") 
    draw_mountain(100, 150, 300, 250, "#808080") 
    draw_mountain(220, 80, 250, 250, "#a0a0a0")  
    
    
    draw_mountain(450, 100, 200, 250, "#a0a0a0") 
    draw_mountain(350, 150, 250, 250, "#c0c0c0") 
    draw_mountain(500, 150, 300, 250, "#808080") 
    draw_mountain(380, 80, 250, 250, "#a0a0a0")  

    # 4. Draw Lightning 
    #Written by Ryan
    lightning(95, 50, scale=0.3)    
    lightning(390, 48, scale=0.22)
    
    #Written by Lionel with some AI to help tidy things up
    #Clouds
    set_fill_color("white")
    set_outline_color("#cccccc")   
    set_line_thickness(1)

    # Cloud 1 — Left side 
    fill_circle(80,  65, 30)
    fill_circle(110, 50, 38)
    fill_circle(145, 57, 28)
    fill_circle(170, 65, 22)

    # Cloud 2 — Right side
    fill_circle(380, 55, 22)
    fill_circle(405, 43, 30)
    fill_circle(435, 50, 24)
    fill_circle(458, 58, 18)


   
    #Written by Ryan
    # 6. Fill the ground base
    set_fill_color("#41980a") 
    set_outline_color("")
    fill_rectangle(0, 250, 600, 150)
    #Draw Rain
    
    draw_rain(num_drops=180, max_y=250)

    # 7. Draw Horizon Line
    #Written by Ryan
    set_outline_color("black")
    set_line_thickness(1)
    draw_line(0, 250, 600, 250)
    
    # 8. Draw Forest
    #Written by Justin with some AI to help tidy things up
    for x in range(30, 550, 85):
        set_fill_color("brown")  
        fill_rectangle(x, 260, 20, 60)
        
        set_fill_color("#0B6623")
        set_outline_color("black")
        fill_triangle(x - 30, 275, x + 50, 275, x + 10, 200)
        fill_triangle(x - 22, 240, x + 42, 240, x + 10, 170)    
    #9. Draw Chicken
    #Written by James with AI to draw the the chicken
    draw_chicken(370, 320, 1.0, "white")  # Standard size white chicken
    draw_chicken(450, 340, 0.4, "yellow") # Tiny yellow baby chick nearby
    fill_triangle(x - 22, 240, x + 42, 240, x + 10, 170)
        
    #Function Call of Dinosaur
    draw_trex(200, 300, 4, "darkgreen", "right")
  
    draw_meteor(50, 40, 10)
    draw_meteor(120, 70, 8)
    draw_meteor(210, 50, 12)
    draw_meteor(300, 90, 9)
    draw_meteor(380, 45, 14)
    draw_meteor(470, 80, 10)
    draw_meteor(540, 35, 11)
        
if __name__ == "__main__":
    # Start the single combined canvas window
    start(draw_picture, 600, 400)
