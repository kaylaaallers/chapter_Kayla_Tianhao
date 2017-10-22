import turtle
tess = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess.pensize(3)

def square_1(t,sz):
    
    for i in range(4):
       t.forward(sz)
       t.right(90)
size=20       
for i in range(5):
    
    square_1(tess,size)
    size=size+20
    tess.penup()
    tess.left(180)
    tess.forward(10)
    tess.right(90)
    tess.forward(10)
    tess.right(90)
    tess.pendown()



       



