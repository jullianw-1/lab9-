
"""

Jullian Wald 01/27/26


project3.py - Refactored Turtle Graphics Scene (Project 3)

Improvements made (summary):
- Broke the large draw_scene(t) body into smaller, single-responsibility functions:
  draw_sun, draw_house, draw_tree, draw_river_and_pond, draw_cloud, etc.
- Removed redundancy by creating helper functions (e.g., draw_house,
  draw_cloud) so multiple instances can be created with different sizes/positions.
- Reused the original drawing functions (draw_rectangle, draw_triangle,
  draw_circle, draw_hexagon) from Project 2 without changing their signatures.
- Kept the first displayed scene identical to the original Project 2 output by
  preserving coordinates and visual properties; added an optional enhanced scene
  that populates the world with additional shapes after user confirmation.
- Added comments and clearer organization to improve readability and maintainability.

Usage:
- Run this script. The original Project 2 scene will appear first.
- A dialog will ask whether you'd like to draw the enhanced, more populated scene.
  Type 'y' (or 'Y') to add the enhanced elements; anything else will leave the
  original scene as-is.
"""

import turtle
import math

# --- Original starter functions (kept unchanged in signature/behavior) ---

def setup_turtle():
    t= turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("turtle Graphics Assignment")
    return t, screen

# definitions of shapes
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

def draw_square(t, size, fill_color = None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_triangle(t, size, fill_color = None):
    if fill_color:
         t.fillcolor(fill_color)
         t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, radius, fill_color = None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

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

def draw_curve(t, length, curve_factor, segments=100):
    segment_length = length/segments
    original_heading = t.heading()

    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i/segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)

    t.setheading(original_heading)

# --- Refactored helper functions and organization ---

# Drawing atomic composite figures using the primitives above.
def draw_sun(t, x, y, radius=50, color="yellow"):
    """Draws the sun at (x,y) using draw_circle."""
    jump_to(t, x, y)
    draw_circle(t, radius, fill_color=color)

def draw_house(t, x, y, width=100, height=100,
               body_color="brown", roof_color="grey"):
    """
    Draws a house where (x,y) is the lower-left corner of the rectangular body.
    The roof triangle is positioned to match the original Project 2 layout.
    """
    # Body
    jump_to(t, x, y)
    draw_rectangle(t, width, height, fill_color=body_color)
    # Roof: original code used a triangle start offset (-30 on x, +height on y)
    roof_start_x = x - (width * 0.3)  # matches original -30 when width=100
    roof_start_y = y + height
    jump_to(t, roof_start_x, roof_start_y)
    # size of triangle should match original 60 when width==100
    roof_size = (width / 100) * 60
    draw_triangle(t, roof_size, fill_color=roof_color)

def draw_tree(t, x, y, trunk_width=20, trunk_height=40,
              foliage_size=60, trunk_color="saddlebrown",
              foliage_color="lightgreen"):
    """
    Draws a simple stylized tree. (x,y) is lower-left of trunk (as in Project 2).
    Foliage triangle is positioned to match the original layout.
    """
    jump_to(t, x, y)
    draw_rectangle(t, trunk_width, trunk_height, fill_color=trunk_color)
    foliage_start_x = x - (foliage_size - trunk_width) / 2  # center foliage over trunk
    foliage_start_y = y
    # original project positioned foliage at x-20 relative to trunk x (when trunk_width=20)
    # So using foliage_start_x = x - 20 for default parameters matches original layout:
    if trunk_width == 20 and foliage_size == 60:
        foliage_start_x = x - 20
    jump_to(t, foliage_start_x, foliage_start_y)
    draw_triangle(t, foliage_size, fill_color=foliage_color)

def draw_hexagon_pond(t, x, y, size=40, color="darkblue"):
    """Draw a hexagon 'pond' using draw_hexagon."""
    jump_to(t, x, y)
    draw_hexagon(t, size, fill_color=color)

def draw_river(t, start_x, start_y, length=600, curve_factor=0.1, heading=-60):
    """
    Draw the meandering river; leaves heading restored to original after drawing.
    This preserves the original river appearance.
    """
    jump_to(t, start_x, start_y)
    t.setheading(heading)
    draw_curve(t, length, curve_factor)
    t.setheading(0)

def draw_cloud(t, x, y, scale=1.0):
    """
    Draws a simple cloud made of three overlapping filled circles.
    (x,y) will be the leftmost circle center.
    scale scales the radii and offsets.
    """
    radius = 15 * scale
    # three overlapping puffs
    jump_to(t, x, y)
    draw_circle(t, radius, fill_color="white")
    jump_to(t, x + 1.2 * radius, y + 0.2 * radius)
    draw_circle(t, radius * 0.9, fill_color="white")
    jump_to(t, x + 2.4 * radius, y)
    draw_circle(t, radius, fill_color="white")

def draw_person(t, x, y, scale=1.0, color="black"):
    """
    Draw a small stick figure for added detail in the enhanced scene.
    (x,y) is the feet position.
    """
    jump_to(t, x, y)
    t.setheading(90)  # face upward
    t.pencolor(color)
    # legs
    t.forward(10 * scale)
    t.right(30)
    t.forward(10 * scale)
    t.backward(10 * scale)
    t.left(60)
    t.forward(10 * scale)
    t.backward(10 * scale)
    t.right(30)
    # body
    t.forward(20 * scale)
    # arms
    t.right(30)
    t.forward(10 * scale)
    t.backward(10 * scale)
    t.left(60)
    t.forward(10 * scale)
    t.backward(10 * scale)
    t.right(30)
    # head
    t.forward(10 * scale)
    jump_to(t, t.xcor(), t.ycor())
    # head as small circle
    jump_to(t, t.xcor(), t.ycor())
    t.pencolor("black")
    t.fillcolor("peachpuff")
    t.begin_fill()
    t.circle(4 * scale)
    t.end_fill()

# --- Scene composition functions ---

def draw_scene(t):
    """
    Refactored draw_scene that composes the original Project 2 elements using
    the helper functions above. It preserves the exact positions/colors/sizes
    so the first displayed scene matches Project 2.
    """
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # draw sun (original: jump_to(t, -200,150); draw_circle(t, 50, fill_color="yellow"))
    draw_sun(t, -200, 150, radius=50, color="yellow")

    # draw the house (original rectangle at -100,-50 size 100x100, roof at -130,50 size 60)
    draw_house(t, -100, -50, width=100, height=100,
               body_color="brown", roof_color="grey")

    # draw tree (original: trunk at 100,-50 size 20x40; foliage triangle at 80,-50 size 60)
    draw_tree(t, 100, -50, trunk_width=20, trunk_height=40,
              foliage_size=60, trunk_color="saddlebrown", foliage_color="lightgreen")

    # draw river (original)
    draw_river(t, -300, -100, length=600, curve_factor=0.1, heading=-60)

    # draw hexagon pond (original: jump_to(t,-270, -80); draw_hexagon(t, 40, fill_color="darkblue"))
    draw_hexagon_pond(t, -270, -80, size=40, color="darkblue")


def enhance_scene(t):
    """
    Populate the scene with additional composite figures to demonstrate reuse
    of the refactored functions. This function is called only if the user
    requests the enhanced scene. It adds houses, trees, clouds, people, etc.
    """
    screen = t.getscreen()
    # Add a few more houses in a row
    house_positions = [(-250, -50), (0, -50), (200, -50)]
    house_colors = [("sandybrown", "maroon"), ("lightyellow", "darkred"), ("burlywood", "slategray")]
    for (pos, cols) in zip(house_positions, house_colors):
        x, y = pos
        body_col, roof_col = cols
        draw_house(t, x, y, width=80, height=80, body_color=body_col, roof_color=roof_col)

    # Add a cluster of trees
    tree_positions = [(-220, -60), (-160, -60), (40, -60), (260, -60)]
    for i, (x, y) in enumerate(tree_positions):
        scale = 1.0 if i % 2 == 0 else 0.8
        draw_tree(t, x, y, trunk_width=int(20*scale), trunk_height=int(35*scale),
                  foliage_size=int(50*scale))

    # Add clouds across the sky
    cloud_positions = [(-100, 210), (0, 230), (120, 200), (220, 240)]
    for i, (cx, cy) in enumerate(cloud_positions):
        draw_cloud(t, cx, cy, scale=1.2 if i % 2 == 0 else 0.9)

    # Add a few people near the river/pond
    people_positions = [(-200, -110), (-150, -120), (-90, -110), (50, -110)]
    for idx, (px, py) in enumerate(people_positions):
        draw_person(t, px, py, scale=0.9 if idx % 2 == 0 else 0.7)

    # Add a small boat on the river (very simple rectangle hull + small triangular sail)
    jump_to(t, -50, -140)
    t.setheading(0)
    t.fillcolor("sienna")
    t.begin_fill()
    # boat hull using rectangle primitive (we'll draw manually to keep proportions)
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(10)
        t.right(90)
    t.end_fill()
    # sail
    jump_to(t, -20, -130)
    t.pencolor("black")
    t.fillcolor("white")
    t.begin_fill()
    t.left(60)
    t.forward(20)
    t.left(60)
    t.forward(20)
    t.left(60)
    t.end_fill()
    t.setheading(0)

    # Add decorative small ponds made of hexagons
    extra_pond_positions = [(-320, -60), (180, -90)]
    for (px, py) in extra_pond_positions:
        draw_hexagon_pond(t, px, py, size=20, color="deepskyblue")

# --- Main entry point ---

def main():
    t, screen = setup_turtle()
    # Draw the first scene which must match Project 2 exactly
    draw_scene(t)

    # Prompt user if they'd like to see an enhanced, more populated scene.
    # Use a simple modal dialog so the first screenshot can be taken before enhancement.
    answer = screen.textinput("Enhance scene", "Type 'y' to draw enhanced scene (or Cancel to keep original):")
    if answer and answer.strip().lower() == 'y':
        enhance_scene(t)
    # Keep the window open
    screen.mainloop()


if __name__ == ("__main__"):
    main()
