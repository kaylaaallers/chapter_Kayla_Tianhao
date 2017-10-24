import turtle

def drawPoly(t, ss, sz):
    """Make turtle t draw a polygon with ss number of sides of side sz."""
    for i in range(ss):
        t.forward(sz)
        t.left(float(360/ss))

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)
    
wn = turtle.Screen()

tess = turtle.Turtle()
tess.pensize(3)

drawEquitriangle(tess, 100)

wn.exitonclick()