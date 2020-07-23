##Harrison Pierce
##This program took me a VERY long time to complete but here it is!
##Prints a checkerboard that is 5x5


import turtle
turtle.speed(20) ##set turtle faster

i = 1 ##set i to 1

for row in range (5):   ##used to loop 5 times for each row
    column = 0          ##set and reset column/square to 0 for every iteration of loop
    square = 0

    oddevenrow = (row % 2)  ##Set variable for determining if row is even or odd

    if (oddevenrow) == 1:   ##if row is odd, enter this if statement
        for column in range(5): ##loop for each column in the loop
            fill2 = column % 2  ## determine if the column is even or odd
  
    
            for square in range(4): ##Loop for printing the square unfilled
                turtle.forward(50)
                turtle.left(90)

        
            if (fill2 == 0):        ##if fill is even, enter this if statement
                turtle.begin_fill()
            
                for square in range(4):    ##Loop for printing the square filled
                    turtle.forward(50)  
                    turtle.left(90)     
            
                turtle.end_fill()
            turtle.forward(50)  
      
        turtle.penup()              ##here we return to the left side and go down 
        turtle.goto(0, (-50)*i)     ## the y axis the appropriate amount for the row it is on
        turtle.pendown()
        i = i + 1                   ##add 1 to i so that next time around the multiplier
                                    #in the 'goto' statement is appropriate



    if (oddevenrow) == 0:           ##When the row is even, enter this loop and repeat the same
        for column in range(5):     ##as above except staggered filling
            fill2 = column % 2
  
        
            for square in range(4):
                turtle.forward(50)
                turtle.left(90)

        ##--------------------------
            if (fill2 == 1):
                turtle.begin_fill()
            ##----------------------
                for square in range(4): 
                    turtle.forward(50)  
                    turtle.left(90)     
            ##----------------------
                turtle.end_fill()
            turtle.forward(50)
        ##--------------------------
        turtle.penup()
        turtle.goto(0, (-50)*i)
        turtle.pendown()
        i = i + 1

  
turtle.done()
