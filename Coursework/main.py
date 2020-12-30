from graphics import *

def integerValidation(requestMessage):
    while True:
        try:
            validInteger = int(input(requestMessage))
        except ValueError as verr:
            print("Please enter a valid integer.", verr)
            continue
        except Exception as ex:
            print("Please enter a valid input.", ex)
            continue
        return validInteger

def drawPolygon(color,px1,py1,px2,py2,px3,py3):
    """ Draws a polygon shape depending on the 6 points input. As of yet this
    is only used to draw the triangles for pattern1.

    Args:
        color (string): Contains a string which is translated to a colour for
        tkinter.
        px1 (int): Point 1 X axis.
        py1 (int): Point 1 Y axis.
        px2 (int): Point 2 X axis.
        py2 (int): Point 2 Y axis.
        px3 (int): Point 3 X axis.
        py3 (int): Point 3 Y axis.
    """    
    triangle = Polygon(Point(px1,py1),Point(px2,py2),Point(px3,py3))
    triangle.setFill(color)
    triangle.draw(win)

def pattern1(color, grid_pos_x, grid_pos_y):
    """ Draws superframe of the triangle pattern as defined in the coursework 
    PDF.

    Args:
        color ([type]): [description]
        grid_pos_x ([type]): [description]
        grid_pos_y ([type]): [description]
    """
    for y in range(grid_pos_y,grid_pos_y+5):
        if not y%2 == 0:
            drawPolygon(color,grid_pos_x,y,0.5+grid_pos_x,y,grid_pos_x,1+y)
            for x in range(grid_pos_x,grid_pos_x+4):
                drawPolygon(color,0.5+x,y,1.5+x,y,1+x,1+y)
            drawPolygon(color,grid_pos_x+4.5,y,0.5+grid_pos_x+4.5,y,grid_pos_x+5,1+y)
        else:
            for x in range(grid_pos_x,grid_pos_x+5):
                drawPolygon(color,x,y,1+x,y,0.5+x,1+y)

def pattern2(color, grid_pos_x, grid_pos_y):
    """ Draws Superframe of the circular patten as defined in the coursework 
    PDF.

    Args:
        color (string): Pointer to the string containing a colour that is
        translated by the tkinter library.
        grid_pos_x (int): X axis for superframe on grid.
        grid_pos_y (int): Y axis for superframe on grid.
    """    
    for y in range(grid_pos_y,grid_pos_y+5):
        for x in range(grid_pos_x,grid_pos_x+5):
            triangle = Circle(Point(x+0.5,y+0.5),0.5)
            if not y%2 == 0:
                triangle.setOutline(color)
            else:
                triangle.setFill(color)
            triangle.draw(win)

available_colors=["red", "green", "blue", "magenta", "orange", "cyan"]
iteration = 0
chosen_colors=[]

# Request the height and width with integer validation.
while True:
    dimention=integerValidation("Height and Width of the patches >> ")
    if dimention==5 or dimention==7:
        print(dimention*dimention)
        break
    else:
        print("Only 5 or 7 mateyyy.")

# Request the user pick the colours from the list below.
print("Enter three colours from the table below, two of which must be unique.")
print("0: red, \n1: green, \n2: blue, \n3: magenta, \n4: orange, \n5: cyan")

while iteration < 3:

    # User input range validation.
    add_color=integerValidation(">> ")
    if not (add_color >= 0 and add_color < len(available_colors)):
        print("Please enter a number in the range specified above.")
        continue
    
    # Validate the users unique colour rule.
    if chosen_colors.count(available_colors[add_color]) > 1:
        print("You need to add another unique colour. Try again.")
    else:
        chosen_colors.append(available_colors[add_color])
        iteration += 1

# Output all the colours chosen.
print(chosen_colors)

# 512 resolution to display.
win = GraphWin("Patterns",500,500)

# 25,25 max grid size. 5 pixels per square, 5 squares.
win.setCoords(0.0, 0.0, dimention*dimention, dimention*dimention)
pattern1("blue", 0, 20)
pattern1("blue", 5, 20)
pattern2("red", 10, 20)
pattern2("red", 15, 20)
pattern2("green", 20, 20)
breaker=input("Enter any key to exit... ")