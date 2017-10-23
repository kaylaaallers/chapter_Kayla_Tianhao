import turtle
tess=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightgreen")
tess.pensize(3)

def square_1(t,sz):
    for i in range(4):
        t.forward(sz)
        t.right(90)
sz=100
for i in range (20):
    square_1(tess,sz)
    tess.right(18)
    
    

