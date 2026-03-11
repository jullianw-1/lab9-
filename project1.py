#--------------------------
# Name: Jullian Wald
# Date: January 14th 2026
# Project: CS110 project 1- turtle graphic scene
# description:
# This program creates a simple nature scene using turtle graphics
# The scene includes a sky, sun, multiple trees, and clouds
# demonstrates the use of variables,loops, conditionals, and comments. 
#---------------------------


import turtle

#screen setup(background)

screen = turtle 
screen.bgcolor("skyblue") # Set background color

#create the turtle 
t= turtle.Turtle()
t.speed(0)
t.hideturtle()

#variables

sun_radius=50 
tree_height=100
num_clouds=3
grass_color="lightgreen"

#Draw the sun

t.penup()
t.goto(200, 150)
t.pendown()
t.color("orange")
t.begin_fill()

#loop to draw circle (sun)
for i in range(36):
    t.forward(sun_radius)
    t.left(10)

t.end_fill()

#draw grass

t.penup()
t.goto(-400,-150)
t.pendown()
t.color("lightgreen")
t.begin_fill()

#rectangle for grass
for i in range(2):
    t.forward(800)
    t.right(90)
    t.forward(200)
    t.right(90)

t.end_fill()

#draw trees using loop 

x_position = -250

for i in range(3):
    t.penup()
    t.goto(x_position,-150)
    t.pendown()
#Tree trunk
t.color("brown")
t.begin_fill()
for j in range(2):
    t.forward(30)
    t.left(90)
    t.forward(tree_height)
    t.left(90)
t.end_fill()

# Tree leaves
t.penup()
t.goto(x_position, -150 + tree_height)  # move to top of trunk
t.pendown()
t.color("darkgreen")
t.begin_fill()

# Draw a leafy canopy using a circle
t.circle(40)  # radius 40, adjust for size

t.end_fill()

# conditions to slightly vary tree loops
tree_number = i 
if tree_number==0 or tree_number==2:
    leaf_size = 80
else:
    leaf_size = 60

big_tree = True
if big_tree == True:
    leaf_size = 80
    big_tree = False
else:
    leaf_size = 60
    big_tree = True
t.end_fill()
x_position += 200 # move to the next tree position 

#draw clouds

cloud_x = -200
for i in  range (num_clouds):
    t.penup()
    t.goto(cloud_x, 150)
    t.pendown()
    t.color("white")
    t.begin_fill()

    #Cloud shape using a loop 
for j in range (6):
    t.circle(20)
    t.penup()
    t.forward(25)
    t.pendown()
t.end_fill()
cloud_x += 200 



def draw_tree(x_position, tree_height):
    # Draw trunk
    t.penup()
    t.goto(x_position, -150)
    t.pendown()
    t.color("sienna")  # brown trunk
    t.begin_fill()
    t.goto(x_position + 20, -150)
    t.goto(x_position + 20, -150 + tree_height)
    t.goto(x_position, -150 + tree_height)
    t.goto(x_position, -150)
    t.end_fill()
    
    # Draw leaves (canopy)
    for dx, dy in [(-20, 0), (20, 0), (0, 30)]:
        t.penup()
        t.goto(x_position + dx + 10, -150 + tree_height + dy)  # +10 centers on trunk
        t.pendown()
        t.color("darkgreen")
        t.begin_fill()
        t.circle(30)
        t.end_fill()

# Draw multiple trees
tree_positions = [-200, -100, 0, 100, 200]  # x positions
tree_heights = [80, 100, 90, 120, 70]       # different heights

for x, h in zip(tree_positions, tree_heights):
    draw_tree(x, h)


#
#Finish 
#
screen.mainloop()
