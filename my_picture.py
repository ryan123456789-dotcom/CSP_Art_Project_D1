import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    
    # Fill the background
    sg.fill_background("white")
    
    # make some variables available
    colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]
    
    triangle_height = height/5
    triangle_width = width / 3
    
    # Draw the tesselation
    # code for red triangles
    sg.set_fill_color(colors[0])
    
    # call fill
    sg.fill_circle(450, 50,50)

    # draw horizon
    sg.set_outline_color("black")
    sg.set_line_thickness(1)
    sg.draw_line(0, 150, 600, 150)


    #James Mountain 
    sg.set_line_thickness(1)
    sg.set_outline_color("grey")
    sg.draw_mountain(150, 100, 200, 250, "#a0a0a0") # Background mountain
    sg.draw_mountain(250, 150, 250, 250, "#c0c0c0") # Foreground mountain
    
    
    sg.draw_mountain(100, 150, 300, 250, "#808080") # Wide, medium mountain on the left
    sg.draw_mountain(220, 80, 250, 250, "#a0a0a0")  # Taller mountain overlapping it




if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
