import turtle

def draw_square(some_turtle):

  for i in range(1,5):
    some_turtle.forward(200)
    some_turtle.right(90)
def draw_art():
    window=turtle.Screen()
    window.bgcolor("yellow")
    #turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(6)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
        window.exitonclick()
draw_art()
