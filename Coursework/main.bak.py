from graphics import *

available_colors=["red", "green", "blue", "magenta", "orange", "cyan"]
portsmouth_id="UP2022742"

def integerValidation(requestMessage):
    """integerValidation validates the integer input if the input is incorrect
    it will request an input again. Once successful it will exit and return.

    Args:
        requestMessage (string): Contains the input message for the user to
        follow.

    Returns:
        [int]: A valid integer value.
    """    
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

def drawPolygon(color,px1,py1,px2,py2,px3,py3,win):
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

def penultimate_digit_pattern0(color, grid_pos_x, grid_pos_y, dimention, win):
    """ Draws a pattern defined by penultimate pattern 0 in the specification.
    It does this by iterating through the rows vertically depending on the 
    user dimention.

    Args:
        color ([type]): [description]
        grid_pos_x ([type]): [description]
        grid_pos_y ([type]): [description]
        dimention (int): Gets the height and width of the total grid.
        win (tk.Canvas): A tkinter canvas instance.
    """
    for y in range(grid_pos_y,grid_pos_y+dimention):
        if not y%2 == 0:
            drawPolygon(color,grid_pos_x,y,0.5+grid_pos_x,y,grid_pos_x,1+y,win)
            for x in range(grid_pos_x,grid_pos_x+dimention-1):
                drawPolygon(color,0.5+x,y,1.5+x,y,1+x,1+y,win)
            drawPolygon(color,grid_pos_x+4.5,y,0.5+grid_pos_x+4.5,y,grid_pos_x+5,1+y,win)
        else:
            for x in range(grid_pos_x,grid_pos_x+dimention):
                drawPolygon(color,x,y,1+x,y,0.5+x,1+y,win)

def penultimate_digit_pattern1(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def penultimate_digit_pattern2(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def penultimate_digit_pattern3(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

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
    small_grid = [[0.25,0.25],[0.75,0.25],[0.25,0.75],[0.75,0.75]]
    for y in range(grid_pos_y,grid_pos_y+dimention):
        for x in range(grid_pos_x,grid_pos_x+dimention):
            for pos in small_grid:
                circle = Circle(Point(x+pos[0],y+pos[1]),0.25)
                if (x+y)%2 == 0:
                    circle.setOutline(color)
                else:
                    circle.setFill(color)
                circle.draw(win)  

def penultimate_digit_pattern5(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def penultimate_digit_pattern6(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def penultimate_digit_pattern7(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def penultimate_digit_pattern8(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def penultimate_digit_pattern9(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern0(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern1(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern2(color, grid_pos_x, grid_pos_y, dimention, win):
    """ Draws Superframe of the circular patten as defined in the coursework 
    PDF.
    Args:
        color (string): Pointer to the string containing a colour that is
        translated by the tkinter library.
        grid_pos_x (int): X axis for superframe on grid.
        grid_pos_y (int): Y axis for superframe on grid.
    """    
    for y in range(grid_pos_y,grid_pos_y+dimention):
        for x in range(grid_pos_x,grid_pos_x+dimention):
            triangle = Circle(Point(x+0.5,y+0.5),0.5)
            if not y%2 == 0:
                triangle.setOutline(color)
            else:
                triangle.setFill(color)
            triangle.draw(win)

def final_digit_pattern3(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern4(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")    

def final_digit_pattern5(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern6(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern7(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern8(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

def final_digit_pattern9(color, grid_pos_x, grid_pos_y, dimention, win):
    print("Incomplete.")

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

    # 512 resolution to display.
    win = GraphWin("Patterns",500,500)

    # 25,25 max grid size. 5 pixels per square, 5 squares.
    win.setCoords(0.0, 0.0, dimention*dimention, dimention*dimention)
    drawSuperframe(win, dimention, chosen_colors)

def colourPresent(x,y,chosen_colors,bluex1,bluey1,bluey2,bluex2,bluey3,bluey4,bluex3,bluex4,bluey5,bluex6,bluex7,bluey6,bluey7,bluex8,bluex9,bluey8,bluey9):
    if (x==bluex1 and y >= bluey1 and y < bluey2) or (x==bluex2 and y >= bluey3 and y < bluey4) or (x >= bluex3 and x < bluex4 and y==bluey5):
        return chosen_colors[0]
    elif x >= bluex6 and x < bluex7 and y >= bluey6 and y < bluey7:
        return chosen_colors[1]
    elif x >= bluex8 and x < bluex9 and y >= bluey8 and y < bluey9:
        return chosen_colors[2]
    else:
        return chosen_colors[0]

def modoloPattern(pattern1, pattern2, color,x,y,dimention,win):
    if(x+y)%2 == 0:
        pattern1(color, x, y, dimention, win)
    else:
        pattern2(color, x, y, dimention, win)

def drawSuperframe(win, dimention, chosen_colors):
    """drawSuperFrame

    Args:
        win (tk.Canvas): A tkinter canvas instance.
        dimention (int): Gets the height and width of the total grid.
        chosen_colors (string): The array of colours chosen by the user.
    """ 
    penultimate_pattern = [
        penultimate_digit_pattern0,
        penultimate_digit_pattern1,
        penultimate_digit_pattern2,
        penultimate_digit_pattern3,
        penultimate_digit_pattern4,
        penultimate_digit_pattern5,
        penultimate_digit_pattern6,
        penultimate_digit_pattern7,
        penultimate_digit_pattern8,
        penultimate_digit_pattern9
    ]
    final_pattern= [
        final_digit_pattern0,
        final_digit_pattern1,
        final_digit_pattern2,
        final_digit_pattern3,
        final_digit_pattern4,
        final_digit_pattern5,
        final_digit_pattern6,
        final_digit_pattern7,
        final_digit_pattern8,
        final_digit_pattern9
    ]
    lastThree=portsmouth_id[-3:]   
    for y in range(0,dimention*dimention,dimention):
        for x in range(0,dimention*dimention,dimention):
            if int(lastThree[0])==7:
                if dimention == 5:
                    modoloPattern(penultimate_pattern[int(lastThree[1])], final_pattern[int(lastThree[2])], colourPresent(x,y,chosen_colors,0,0,25,20,0,25,5,20,10,5,20,0,10,5,20,15,25),x,y,dimention,win)
                if dimention == 7:
                    modoloPattern(penultimate_pattern[int(lastThree[1])], final_pattern[int(lastThree[2])], colourPresent(x,y,chosen_colors,0,0,49,42,0,49,7,41,21,7,42,0,21,7,42,28,49),x,y,dimention,win)
            else:
                print("Not requested to be developed.")

if __name__ == "__main__":
    main()

breaker=input("Enter any key to exit... ")