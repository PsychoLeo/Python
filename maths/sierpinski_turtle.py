from turtle import Screen, Turtle, mode, Vec2D


win = Screen()
win.bgcolor('black')
mode('logo')
tur = Turtle()
tur.shape('arrow')
tur.shapesize(0.5, 0.5, 0.5)
tur.color('lime', 'green')
tur.speed(10)
# Turtle.tracer(0, 0)
win.tracer(0, 0)

def points(leng, off=(0, 0), rot=0, ang=60):
  tur.pu()
  yield Vec2D(0, 0) + off
  tur.pd()
  yield Vec2D(0, leng).rotate(ang/2 + rot) + off
  yield Vec2D(0, leng).rotate(-ang/2 + rot) + off
  yield Vec2D(0, 0) + off

def sierpinski(leng=150, depth=3, angle=0):
#   tur.fill(True)
  for i, p in enumerate(points(leng, tur.pos(), angle)):
    tur.goto(p)
    if depth > 1 and i < 3:
      sierpinski(leng/2, depth - 1, i*240 + angle)
      win.update()
#   tur.fill(False)

sierpinski(1000, 8, 180)
win.exitonclick()