import turtle as t

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()

# Functions

def colinput():
    col1 = raw_input("Type the first colour you would like: ")
    col2 = raw_input("Type the second colour you would like: ")
    col3 = raw_input("Type the third colour you would like: ")
    col4 = raw_input("Type the fourth colour you would like: ")
    return (col1, col2, col3, col4)

def tspeedinput():
    pspeed = input("What speed do you want the turtle to move? (Number between 1-10, 10 is fastest, 0 for hyperspeed!): ")
    return pspeed

def tpenspeed(pspeed):
    t1.speed(pspeed)
    t2.speed(pspeed)
    t3.speed(pspeed)
    t4.speed(pspeed)

def tsizeinput():
    psize = input("What size do you want the turtle to be? (Ideally a number between 0 and 10, but it can be anything greater than 0): ")
    return psize

def tpensize(psize):
    t1.pensize(psize)
    t2.pensize(psize)
    t3.pensize(psize)
    t4.pensize(psize)

def circle (turtleNum, col, rad):
    turtleNum.pencolor(col)
    turtleNum.circle(rad)

def square (turtleNum, l, col):
    turtleNum.pencolor(col)
    for i in range (4):
        turtleNum.forward (l)
        turtleNum.left (90)

def doublesquare (turtleNum, l, l2, col):
    turtleNum.pencolor(col)
    for i in range (4):
        turtleNum.forward (l)
        turtleNum.left (90)
        turtleNum.fillcolor(col)
        turtleNum.begin_fill()
        for i in range (4):
            turtleNum.forward (l2)
            turtleNum.left (90)
            
        turtleNum.end_fill()
    
def penup():
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    
def goto_symm(x_coord, y_coord):
    t1.goto(x_coord,y_coord)
    t2.goto(-x_coord,y_coord)
    t3.goto(-x_coord,-y_coord)
    t4.goto(x_coord,-y_coord)

def pendown():
    t1.pendown()
    t2.pendown()
    t3.pendown()
    t4.pendown()

def thide():
    t1.ht()
    t2.ht()
    t3.ht()
    t4.ht()

# Preparation of Variables and Inputs

col1 = 0
col2 = 0
col3 = 0
col4 = 0
pspeed = 0
psize = 0

print "Before we start drawing, lets pick some colors, a pen speed and a pen size!"
col1, col2, col3, col4 = colinput()
pspeed = tspeedinput()
psize = tsizeinput()

# Preparation for Drawing

tpensize(psize)
tpenspeed(pspeed)

penup()
goto_symm(200, 200)
pendown()

# Drawing

circle (t1, col1, 25)
circle (t2, col2, 25)
circle (t3, col3, 25)
circle (t4, col4, 25)

penup()
t1.goto(175, 200)
t2.goto(-225, 200)
t3.goto(-225, -200)
t4.goto(175, -200)
pendown()

square (t1, 50, col1) 
square (t2, 50, col2)
square (t3, 50, col3)
square (t4, 50, col4) 


penup()
t1.goto(0, 25)
t2.goto(-250, 25)
t3.goto(-250, -225)
t4.goto(0, -225)
pendown()


doublesquare(t1, 250, 75, col1)
doublesquare(t2, 250, 75, col2)
doublesquare(t3, 250, 75, col3)
doublesquare(t4, 250, 75, col4)

thide()

