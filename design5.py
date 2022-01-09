# import turtle
# w = turtle.Screen()
# w.title('Spiral Helix')
# w.bgcolor('black')

# colors = ['red','blue','purple','green','orange','yellow']

# t = turtle.pen()
# t.speed(100)

# for x in range(360):
#     color = colors[x % len(colors)]
#     t.pencolor(color)
#     t.width(x / 100+1)
#     t.forward(x)
#     t.left(59)


# turtle.done()

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()