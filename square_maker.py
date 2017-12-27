import turtle


def draw_square(some_object):

    for i in range(4):
        some_object.forward(100)
        some_object.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    Alex = turtle.Turtle()
    Alex.shape("turtle")
    Alex.color("green")
    Alex.speed(10)
    for i in range(0,36):
        draw_square(Alex)
        Alex.right(10)

    window.exitonclick()


draw_art()


