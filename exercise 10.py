import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
star = turtle.Turtle()
star.speed(5)
star.color("hotpink")
side=5
star.penup()
star.goto(0,0) 
star.pendown()
star.pensize(3)
def star1 (t):
    for i in range(5):
        
        t.forward(100)
        t.right(144)
        
sz=350        
for b in range(5):
    star1 (star)
    star.penup()
    star.left(144)
    star.forward(350)
    star.pendown()
    


    
    
    