import turtle

def mystar (size, filled) :
    t = turtle.Pen ()
    t.color (1, 0, 1)
    if filled == True :
        t.begin_fill ()
    for x in range (1, 19) :
        t.forward (size)
        if x % 2 == 0 :
            t.left (175)
        else :
            t.left (225)
    if filled == True :
        t.end_fill ()
        
def octagon (size) :
    t = turtle.Pen ()
    t.begin_fill ()
    for i in range (8) :
        t.forward (size)
        t.left (45)
    t.end_fill ()
    
'''
def draw_star (size, branches) :
    t = turtle.Pen ()
    for i in range (1, 2*branches+1) :
        t.forward (size)
        if i % 2 == 0 :
            t.left (170)
        else :
            t.left ((360-10*branches)/branches)
'''


def draw_star (size, branches) :
    t = turtle.Pen ()
    angle = 360 / branches
    for x in range(0, branches):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(180-(angle * 2))
        
T = turtle.Pen ()
for i in range(100):
    T.circle(10+i)