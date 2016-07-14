import math
import turtle as t

def init_drawman(x=0, y=0):
    t.penup()
    t.goto(x,y)
    drawman_scale(3)

def drawman_scale(sc):
    global _scale
    _scale = sc

def scale(var):
    return var*_scale

def test_drawman():
    to_point()
    pen_down()
    for i in range(5):
        on_vector(0, 20)
        on_vector(-20, -20)
    pen_up()
    to_point()
    t.mainloop()

def the_end():
    t.mainloop()

def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(x=0, y=0):
    if x == 0 :
        t.left(90)
        t.forward(scale(y))
        t.right(90)
    elif x > 0:
        t.left(math.atan(y/x)*180/math.pi)
        t.forward(scale(math.sqrt(x*x+y*y)))
        t.right(math.atan(y/x)*180/math.pi)
    else: # x < 0
        t.left(math.atan(y/x)*180/math.pi+180)
        t.forward(scale(math.sqrt(x*x+y*y)))
        t.right(math.atan(y/x)*180/math.pi+180)

def to_point(x=0, y=0):
    t.goto(scale(x), scale(y))

init_drawman()
if __name__ == "__main__":
    test_drawman()



