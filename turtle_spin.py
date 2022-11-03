import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen ().bgcolor("black")
t.pensize(2)
t.speed(0)
n=100
h=0
for i in range(85):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.right(120)
    t.circle(i*1.2, -180)
    t.circle(i, 180)
    t.circle(i, 60)

turtle.done()