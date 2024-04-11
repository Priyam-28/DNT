import turtle


screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed("slowest")  

def draw_D():
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.circle(50, -180)

def draw_N():
    t.penup()
    t.goto(20, 0)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(150)
    t.forward(115)
    t.left(150)
    t.forward(100)

def draw_T():
    t.penup()
    t.goto(130, 0) 
    t.pendown()
    t.forward(100)  
    t.right(90)  
    t.forward(40)  
    t.backward(80)

draw_D()
draw_N()
draw_T()


turtle.done()
