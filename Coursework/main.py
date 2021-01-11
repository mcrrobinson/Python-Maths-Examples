from graphics import *

# Canvas Size in pixels.
CANVAS_SIZE=500

# Number of colours for the user to enter.
NUMBER_OF_COLORS_ENTERED=3

# Available Tkinter translatable colours.
available_colors=["red", "green", "blue", "magenta", "orange", "cyan"]

# GLOBALS
selected_dimention=[]
pattern=[]

def round_down(num,divisor):
    """round_down rows the value down by a divisor value.

    Args:
        num (int): An integer.
        divisor (int): A number to divise by.

    Returns:
        [int]: A rounded down value byt he divisor.
    """        
    return num - (num%divisor)

def integerValidation(requestMessage):
    """integerValidation validates the integer input if the input is 
    incorrect it will request an input again. Once successful it will exit 
    and return.

    Args:
        requestMessage (string): Contains the input message for the user to
        follow.

    Returns:
        [int]: A valid integer value.
    """    
    while True:
        validInteger = input(requestMessage)
        if validInteger.isdigit():
            return int(validInteger)
        print("Please enter a valid integer.")

def drawPolygon(color,px1,py1,px2,py2,px3,py3,win):
    """ Draws a polygon shape depending on the 6 points input. As of yet 
    this is only used to draw the triangles for pattern1.

    Args:
        color (string): Contains a string which is translated to a colour 
        for tkinter.
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

def penultimate_digit_pattern4(color, grid_pos_x, grid_pos_y, dimention, win):
    """ Draws a pattern defined by the penultimate pattern 4 in the
    specification. Firstly iterates vertically for the Y axis then iterates
    horizontally for the x axis.

    Args:
        color (string): Pointer to the string containing a colour that is
        translated by the tkinter library.
        grid_pos_x (int): X axis for superframe on grid.
        grid_pos_y (int): Y axis for superframe on grid.
        dimention (int): Gets the height and width of the total grid.
        win (tk.Canvas): A tkinter canvas instance.
    """

    # Constants based on dimention.
    circle_padding=dimention/5

    small_circle_coordinate = [
        {"x":0.25,"y":0.25},
        {"x":0.75,"y":0.25},
        {"x":0.25,"y":0.75},
        {"x":0.75,"y":0.75}
    ]

    # Would prefer to have used enumerate but can't increment a for loop by
    # a decimal integer which could happen as a division is happening. 
    # Because of this I have decided to use while loops which can handle the
    # decimal incrementation and a seperate variable called mod_counter which
    # increments by 1 every iteration to get odd and even numbers.
    y,y_mod_counter = 0,0
    while y < dimention:
        x,x_mod_counter = 0,0
        while x < dimention:
            for pos in small_circle_coordinate:
                circle=Circle(Point(
                    grid_pos_x+x+circle_padding*pos['x'],
                    grid_pos_y+y+circle_padding*pos['y']
                ),circle_padding*0.25)
                if(x_mod_counter+y_mod_counter)%2==0:
                    circle.setOutline(color)
                else:
                    circle.setFill(color)
                circle.draw(win)
                pattern.append({
                    "x":grid_pos_x+x+circle_padding*pos['x'],
                    "y":grid_pos_y+y+circle_padding*pos['y'],
                    "shape":circle
                })
            x_mod_counter += 1
            x += circle_padding
        y_mod_counter += 1
        y += circle_padding

def final_digit_pattern2(color, grid_pos_x, grid_pos_y, dimention, win):
    """ Draws Superframe of the circular patten as defined in the coursework 
    PDF.
    Args:
        color (string): Pointer to the string containing a colour that is
        translated by the tkinter library.
        grid_pos_x (int): X axis for superframe on grid.
        grid_pos_y (int): Y axis for superframe on grid.
    """
    # Constants based on dimention.
    circle_radius=dimention/10
    circle_padding=dimention/5

    # Offset because the circle starts at the center.
    y = circle_radius
    mod_counter = 0
    while y < dimention:
        x = circle_radius
        while x < dimention:
            circle=Circle(Point(
                grid_pos_x+x,
                grid_pos_y+y
            ),circle_radius)
            if not mod_counter%2==0:
                circle.setOutline(color)
            else:
                circle.setFill(color)
            circle.draw(win)
            pattern.append({
                "x":grid_pos_x,
                "y":grid_pos_y,
                "shape":circle
            })
            x += circle_padding
        mod_counter += 1
        y += circle_padding

def delete_square(event,dimention):
    """delete_square uses the selected block and deletes it by drawing over
    with a blank polygon.

    Args:
        event (Point): Contains current value of X and Y relative to the
        cursor.
        dimention (int) Number of patterns per superframe.
    """        
    if selected_dimention:
        for objects in selected_dimention:
            objects["shape"].undraw()

def returnPatternColour(x,y,chosen_colors,bluex1,bluey1,bluey2,bluex2,bluey3,bluey4,
bluex3,bluex4,bluey5,bluex6,bluex7,bluey6,bluey7,bluex8,bluex9,bluey8,bluey9):
    if (x==bluex1 and y >= bluey1 and y < bluey2) or (x==bluex2 and y >= bluey3 
    and y < bluey4) or (x >= bluex3 and x < bluex4 and y==bluey5):
        return chosen_colors[0]
    elif x >= bluex6 and x < bluex7 and y >= bluey6 and y < bluey7:
        return chosen_colors[1]
    elif x >= bluex8 and x < bluex9 and y >= bluey8 and y < bluey9:
        return chosen_colors[2]
    else:
        return chosen_colors[0]

def modoloPattern(color,x,y, dimention, win):
    """modoloPattern uses modulus to find out whether or not the integer is
    odd or even.

    Args:
        color (string): Passes in the string that is translated by the 
        graphics wrapper recognised by tkinter.
        x (int): X axis for subframe.
        y (int): Y axis for subframe.
        dimention (int): Number of patterns per superframe.
    """        
    if(x+y)%2 == 0:
        penultimate_digit_pattern4(color, x, y, dimention, win)
    else:
        final_digit_pattern2(color, x, y, dimention, win)

def drawSuperPattern(chosen_colors, dimention, win):
    """drawSuperPattern

    Args:
        win (tk.Canvas): A tkinter canvas instance.
        dimention (int): Gets the height and width of the total grid.
        chosen_colors (string): The array of colours chosen by the user.
    """ 
    for y in range(0,dimention*dimention,dimention):
        for x in range(0,dimention*dimention,dimention):
            if dimention == 5:
                modoloPattern(
                    returnPatternColour(
                        x,y,chosen_colors,
                        0,0,25,20,0,25,5,20,10,5,20,0,10,5,20,15,25
                        ),x,y, dimention,win)
            if dimention == 7:
                modoloPattern(
                    returnPatternColour(
                        x,y,chosen_colors,
                        0,0,49,42,0,49,7,41,21,7,42,0,21,7,42,28,49
                    ),x,y, dimention,win)

    while True:
        mouse=win.getMouse()
        selected_dimention.clear()
        for objects in pattern:
            if (objects["x"]>=round_down(mouse.x,dimention) and 
            objects["x"]<round_down(mouse.x,dimention)+dimention) and (
                objects["y"]>=round_down(mouse.y, dimention) and 
                objects["y"]<round_down(mouse.y, dimention)+dimention
                ):
                selected_dimention.append(objects)

def main():
    iteration = 0
    chosen_colors=[]

    # Request the height and width with integer validation.
    print("Enter a grid size of either: 5 or 7")
    while True:
        dimention=integerValidation("Height and Width of the patches >> ")
        if dimention==5 or dimention==7:
            break
        print("Please enter one of the two options.")

    # Request the user pick the colours from the list below.
    print("Enter three colours from the table below, two of which must be unique.")
    print("0: red, \n1: green, \n2: blue, \n3: magenta, \n4: orange, \n5: cyan")

    # User input range validation.
    while iteration < NUMBER_OF_COLORS_ENTERED:
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

    # 512 resolution to display.
    win = GraphWin("Patterns",CANVAS_SIZE,CANVAS_SIZE)
    win.setCoords(0.0, 0.0, dimention*dimention, dimention*dimention)
    win.focus_set() 
    win.bind('<Delete>', lambda event: delete_square(event, dimention))
    win.pack()       
    drawSuperPattern(chosen_colors, dimention, win)

if __name__ == "__main__":
    main()

breaker=input("Press enter to exit... ")