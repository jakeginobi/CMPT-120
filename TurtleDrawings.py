import turtle as t

t1 = t.Turtle()
t2 = t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()


def tpensize(pens):
    t1.pensize(pens)
    t2.pensize(pens)
    t3.pensize(pens)
    t4.pensize(pens)

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

tpensize(3)
t1.speed(8)
t2.speed(8)
t3.speed(8)
t4.speed(8)

penup()
goto_symm(200, 200)
pendown()

circle (t1, "blue", 25)
circle (t2, "green", 25)
circle (t3, "red", 25)
circle (t4, "yellow", 25)

penup()
t1.goto(175, 200)
t2.goto(-225, 200)
t3.goto(-225, -200)
t4.goto(175, -200)
pendown()

square (t1, 50, "blue") 
square (t2, 50, "green")
square (t3, 50, "red")
square (t4, 50, "yellow") 


penup()
t1.goto(0, 25)
t2.goto(-250, 25)
t3.goto(-250, -225)
t4.goto(0, -225)
pendown()

tpensize(5)

doublesquare(t1, 250, 75, "blue")
doublesquare(t2, 250, 75, "green")
doublesquare(t3, 250, 75, "red")
doublesquare(t4, 250, 75, "yellow")

t1.ht()
t2.ht()
t3.ht()
t4.ht()
