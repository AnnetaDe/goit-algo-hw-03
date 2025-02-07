import turtle


def koch_curve(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(turtle, order - 1, size / 3)
            turtle.left(angle)


def draw_koch_snowflake(turtle, order, size):
    for _ in range(3):
        koch_curve(turtle, order, size)
        turtle.right(120)


def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(6)
    t.penup()
    t.goto(-size / 2, size / (2 * 3**0.5))
    t.pendown()

    draw_koch_snowflake(t, order, size)

    window.mainloop()


draw_koch_curve(3)
