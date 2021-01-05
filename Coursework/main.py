from graphics import *

available_colors=["red", "green", "blue", "magenta", "orange", "cyan"]

class classname(object):
    pass

    def __init__(self):
        self.selected_dimention=[]
        self.pattern=[]
        self.win=None

    def round_down(self,num,divisor):
        """round_down rows the value down by a divisor value.

        Args:
            num (int): An integer.
            divisor (int): A number to divise by.

        Returns:
            [int]: A rounded down value byt he divisor.
        """        
        return num - (num%divisor)

    def integerValidation(self,requestMessage):
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
            try:
                validInteger = int(input(requestMessage))
            except ValueError as verr:
                print("Please enter a valid integer.", verr)
                continue
            except Exception as ex:
                print("Please enter a valid input.", ex)
                continue
            return validInteger

    def drawPolygon(self,color,px1,py1,px2,py2,px3,py3,win):
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

    def penultimate_digit_pattern4(self,color, grid_pos_x, grid_pos_y,dimention):
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
                    circle=Circle(Point(x+pos[0],y+pos[1]),0.25)
                    self.pattern.append([x,y,circle])
                    if (x+y)%2 == 0:
                        circle.setOutline(color)
                    else:
                        circle.setFill(color)
                    circle.draw(self.win)  

    def final_digit_pattern2(self,color, grid_pos_x, grid_pos_y,dimention):
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
                triangle=Circle(Point(x+0.5,y+0.5),0.5)
                self.pattern.append([x,y,triangle])
                if not y%2 == 0:
                    triangle.setOutline(color)
                else:
                    triangle.setFill(color)
                triangle.draw(self.win)

    def delete_square(self,event,dimention):
        """delete_square uses the selected block and deletes it by drawing over
        with a blank polygon.

        Args:
            event (Point): Contains current value of X and Y relative to the
            cursor.
            dimention (int) Number of patterns per superframe.
        """        
        if self.selected_dimention:
            for i in self.selected_dimention:
                i[2].undraw()
            self.pattern[:] = [x for x in self.pattern if not self.selected_dimention[-1][0]>=x[0] and x[0]>=self.selected_dimention[0][0] and self.selected_dimention[-1][1]>=x[1] and x[1]>=self.selected_dimention[0][0]]

    def shift_square_left(self,event,dimention):
        FAILURE=False
        if self.selected_dimention:

            # Check to see if there is an existing object in the square.
            for i in self.pattern:
                if i[0] == self.selected_dimention[0][0]-dimention:
                    FAILURE=True
            if not FAILURE:
                for _ in range(dimention*10):
                    for shape in self.selected_dimention:
                        shape[2].move(-0.1,0)
                    self.win.after(20)
                for shape in self.selected_dimention:
                    shape[0]=shape[0]-dimention
            else:
                print("There is an object in the way.")
                    
    def shift_square_right(self,event,dimention):
        FAILURE=False
        if self.selected_dimention:
            for i in self.pattern:
                if i[0] == self.selected_dimention[0][0]+dimention:
                    FAILURE=True
            if not FAILURE:
                for _ in range(dimention*10):
                    for shape in self.selected_dimention:
                        shape[2].move(0.1,0)
                    self.win.after(20)
                for shape in self.selected_dimention:
                    shape[0]=shape[0]+dimention
            else:
                print("There is an object in the way.")
    def shift_square_up(self,event,dimention):
        FAILURE=False
        if self.selected_dimention:
            for i in self.pattern:
                if i[1] == self.selected_dimention[0][1]+dimention:
                    FAILURE=True
            if not FAILURE:
                for _ in range(dimention*10):
                    for shape in self.selected_dimention:
                        shape[2].move(0,0.1)
                    self.win.after(20)
                for shape in self.selected_dimention:
                    shape[1]=shape[1]+dimention
            else:
                print("There is an object in the way.")

    def shift_square_down(self,event,dimention):
        FAILURE=False
        if self.selected_dimention:
            for i in self.pattern:
                if i[1] == self.selected_dimention[0][1]-dimention:
                    FAILURE=True
            if not FAILURE:
                for _ in range(dimention*10):
                    for shape in self.selected_dimention:
                        shape[2].move(0,-0.1)
                    self.win.after(20)
                for shape in self.selected_dimention:
                    shape[1]=shape[1]-dimention
            else:
                print("There is an object in the way.")

    def main(self):
        iteration = 0
        chosen_colors=[]

        # Request the height and width with integer validation.
        print("Enter a grid size of either: 5 or 7")
        while True:
            dimention=self.integerValidation("Height and Width of the patches >> ")
            if dimention==5 or dimention==7:
                break
            print("Please enter one of the two options.")

        # Request the user pick the colours from the list below.
        print("Enter three colours from the table below, two of which must be unique.")
        print("0: red, \n1: green, \n2: blue, \n3: magenta, \n4: orange, \n5: cyan")

        # User input range validation.
        while iteration < 3:
            add_color=self.integerValidation(">> ")
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
        self.win = GraphWin("Patterns",500,500)
        self.win.setCoords(0.0, 0.0, dimention*dimention, dimention*dimention)
        self.win.focus_set() 
        self.win.bind('<Delete>', lambda event: self.delete_square(event, dimention))
        self.win.bind('<Left>', lambda event: self.shift_square_left(event, dimention))
        self.win.bind('<Right>', lambda event: self.shift_square_right(event, dimention))
        self.win.bind('<Up>', lambda event: self.shift_square_up(event, dimention))
        self.win.bind('<Down>', lambda event: self.shift_square_down(event, dimention))
        self.win.pack()       
        self.drawSuperframe(chosen_colors, dimention)

    def colourPresent(self,x,y,chosen_colors,bluex1,bluey1,bluey2,bluex2,bluey3,bluey4,
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

    def modoloPattern(self,color,x,y, dimention):
        """moduloPattern uses modulus to find out whether or not the integer is
        odd or even.

        Args:
            color (string): Passes in the string that is translated by the 
            graphics wrapper recognised by tkinter.
            x (int): X axis for subframe.
            y (int): Y axis for subframe.
            dimention (int): Number of patterns per superframe.
        """        
        if(x+y)%2 == 0:
            self.penultimate_digit_pattern4(color, x, y, dimention)
        else:
            self.final_digit_pattern2(color, x, y, dimention)

    def drawSuperframe(self, chosen_colors, dimention):
        """drawSuperFrame

        Args:
            win (tk.Canvas): A tkinter canvas instance.
            dimention (int): Gets the height and width of the total grid.
            chosen_colors (string): The array of colours chosen by the user.
        """ 
        for y in range(0,dimention*dimention,dimention):
            for x in range(0,dimention*dimention,dimention):
                if dimention == 5:
                    self.modoloPattern(
                        self.colourPresent(
                            x,y,chosen_colors,
                            0,0,25,20,0,25,5,20,10,5,20,0,10,5,20,15,25
                            ),x,y, dimention)
                if dimention == 7:
                    self.modoloPattern(
                        self.colourPresent(
                            x,y,chosen_colors,
                            0,0,49,42,0,49,7,41,21,7,42,0,21,7,42,28,49
                        ),x,y, dimention)

        while True:
            mouse=self.win.getMouse()
            self.selected_dimention.clear()
            print(mouse.x, mouse.y)
            for objects in self.pattern:
                print(objects)
                if (objects[0]>=self.round_down(mouse.x,dimention) and objects[0]<self.round_down(mouse.x,dimention)+dimention) and (objects[1]>=self.round_down(mouse.y, dimention) and objects[1]<self.round_down(mouse.y, dimention)+dimention):
                    self.selected_dimention.append(objects)

if __name__ == "__main__":
    classname().main()

breaker=input("Enter any key to exit... ")