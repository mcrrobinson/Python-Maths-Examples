from graphics import *

CANVAS_SIZE=500
NUMBER_OF_COLORS_ENTERED=3
AVAILABLE_COLOURS=["red", "green", "blue", "magenta", "orange", "cyan"]

def round_down(num,divisor):
    return num - (num%divisor)

def integerValidation(requestMessage):
    while True:
        validInteger = input(requestMessage)
        if validInteger.isdigit():
            return int(validInteger)
        print("Please enter a valid integer.")

def drawPolygon(color,px1,py1,px2,py2,px3,py3,win):
    triangle = Polygon(Point(px1,py1),Point(px2,py2),Point(px3,py3))
    triangle.setFill(color)
    triangle.draw(win)

def penultimate_digit_pattern4(color, grid_pos_x, grid_pos_y, dimention, all_patterns, win):
    circle_padding=dimention/5
    small_circle_coordinate = [
        {"x":0.25,"y":0.25},
        {"x":0.75,"y":0.25},
        {"x":0.25,"y":0.75},
        {"x":0.75,"y":0.75}
    ]
    
    y,y_mod_counter = 0,0
    while y < dimention:
        x,x_mod_counter = 0,0
        while x < dimention:
            for pos in small_circle_coordinate:
                width=grid_pos_x+x+circle_padding*pos['x']
                height=grid_pos_y+y+circle_padding*pos['y']

                circle=Circle(Point(width,height),circle_padding*0.25)
                if(x_mod_counter+y_mod_counter)%2==0:
                    circle.setOutline(color)
                else:
                    circle.setFill(color)
                circle.draw(win)
                all_patterns.append({"x":width,"y":height,"shape":circle})
            x_mod_counter += 1
            x += circle_padding
        y_mod_counter += 1
        y += circle_padding

def final_digit_pattern2(color, grid_pos_x, grid_pos_y, dimention, all_patterns, win):
    circle_radius=dimention/10
    circle_padding=dimention/5

    y = circle_radius
    mod_counter = 0
    while y < dimention:
        x = circle_radius
        while x < dimention:
            width=grid_pos_x+x
            height=grid_pos_y+y
            
            circle=Circle(Point(width,height),circle_radius)
            if not mod_counter%2==0:
                circle.setOutline(color)
            else:
                circle.setFill(color)
            circle.draw(win)
            all_patterns.append({"x":width,"y":height,"shape":circle})
            x += circle_padding
        mod_counter += 1
        y += circle_padding

def delete_square(selected_dimention):    
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

def modoloPattern(color,x,y, dimention, all_patterns, win):
    if(x+y)%2 == 0:
        penultimate_digit_pattern4(color, x, y, dimention, all_patterns, win)
    else:
        final_digit_pattern2(color, x, y, dimention, all_patterns, win)

def drawSuperPattern(chosen_colors, dimention, all_patterns, win):
    for y in range(0,dimention*dimention,dimention):
        for x in range(0,dimention*dimention,dimention):
            if dimention == 5:
                modoloPattern(
                    returnPatternColour(
                        x,y,chosen_colors,
                        0,0,25,20,0,25,5,20,10,5,20,0,10,5,20,15,25
                        ),x,y, dimention,all_patterns,win)
            if dimention == 7:
                modoloPattern(
                    returnPatternColour(
                        x,y,chosen_colors,
                        0,0,49,42,0,49,7,41,21,7,42,0,21,7,42,28,49
                    ),x,y, dimention,all_patterns,win)

def main():
    iteration = 0
    chosen_colors=[]
    selected_dimention=[]
    all_patterns=[]

    print("Enter a grid size of either: 5 or 7")
    while True:
        dimention=integerValidation("Height and Width of the patches >> ")
        if dimention==5 or dimention==7:
            break
        print("Please enter one of the two options.")

    print("Enter three colours from the table below, two of which must be unique.")
    print("0: red, \n1: green, \n2: blue, \n3: magenta, \n4: orange, \n5: cyan")

    while iteration < NUMBER_OF_COLORS_ENTERED:
        add_color=integerValidation(">> ")
        if not (add_color >= 0 and add_color < len(AVAILABLE_COLOURS)):
            print("Please enter a number in the range specified above.")
            continue

        if chosen_colors.count(AVAILABLE_COLOURS[add_color]) > 1:
            print("You need to add another unique colour. Try again.")
        else:
            chosen_colors.append(AVAILABLE_COLOURS[add_color])
            iteration += 1

    win = GraphWin("Patterns",CANVAS_SIZE,CANVAS_SIZE)
    win.setCoords(0.0, 0.0, dimention*dimention, dimention*dimention)
    win.focus_set()
    win.pack()       
    drawSuperPattern(chosen_colors, dimention, all_patterns, win)

    while True:               
        win.bind('<d>', lambda event: delete_square(selected_dimention)) 
        mouse=win.getMouse()
        selected_dimention.clear()
        for objects in all_patterns:
            if (objects["x"]>=round_down(mouse.x,dimention) and 
            objects["x"]<round_down(mouse.x,dimention)+dimention) and (
                objects["y"]>=round_down(mouse.y, dimention) and 
                objects["y"]<round_down(mouse.y, dimention)+dimention
                ):
                selected_dimention.append(objects)

if __name__ == "__main__":
    main()