







import turtle 
import math

def setup_turtle():
    t= turtle.Turtle()
    t.speed(0) 
    screen = turtle.Screen()
    screen.title("turtle Graphics Assignment")
    return t, screen 
#definintons of shapes 
def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()
#definintons of shapes 
def draw_square(t, size, fill_color = None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()
#definintons of shapes 
def draw_triangle(t, size, fill_color = None):
    if fill_color:
         t.fillcolor(fill_color)
         t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()
#definintons of shapes 
def draw_circle(t, radius, fill_color = None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()
#definintons of shapes 
def draw_hexagon(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(6):
        t.forward(size)
        t.right(60)
    if fill_color:
        t.end_fill()

def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()





def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    screen = t.getscreen()
    screen.bgcolor("skyblue")
    #draw sun 
    jump_to(t, -200,150)
    draw_circle(t, 50, fill_color="yellow")
    #draw the house 
    jump_to(t, -100, -50)
    draw_rectangle(t, 100, 100, fill_color="brown")
    jump_to(t,-130, 50)
    draw_triangle(t, 60, fill_color="grey")
    #draw tree
    jump_to(t, 100, -50)
    draw_rectangle(t, 20, 40, fill_color="saddlebrown")
    jump_to(t, 80, -50)
    draw_triangle(t, 60, fill_color="lightgreen")
    #draw river 
    jump_to(t, -300, -100)
    t.setheading(-60) #set heading for the curve
    draw_curve(t, 600, 0.1)
   #draw hexagon pond 
    t.setheading(0)
    jump_to(t,-270, -80)
    draw_hexagon(t, 40, fill_color="darkblue")

#defining curve
def draw_curve(t, length, curve_factor, segments=100):
    segment_length = length/segments 
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i/segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)
    
    t.setheading(original_heading)
def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()




if __name__ == ("__main__"):
    main()
