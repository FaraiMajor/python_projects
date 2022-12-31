from turtle import Screen, Turtle


tim_the_turtle = Turtle()
tim_the_turtle.shape('turtle')
tim_the_turtle.color("red")
tim_the_turtle.forward(100)
tim_the_turtle.speed("slow")
screen = Screen()

print(tim_the_turtle)


# import turtle  # Outside_In
# wn = turtle.Screen()
# wn.bgcolor("light green")
# wn.title("Turtle")
# skk = turtle.Turtle()
# skk.color("blue")


# def sqrfunc(size):
#     for i in range(4):
#         skk.fd(size)
#         skk.left(90)
#         size = size-5


# sqrfunc(146)
# sqrfunc(126)
# sqrfunc(106)
# sqrfunc(86)
# sqrfunc(66)
# sqrfunc(46)
# sqrfunc(26)


# def star(turtle, size):
#     if size <= 10:
#         return

#     turtle.begin_fill()

#     for _ in range(5):
#         turtle.forward(size)
#         star(turtle, size/3)
#         turtle.left(216)

#     turtle.end_fill()


# screen = Screen()
screen.bgcolor('black')

# turtle = Turtle()
# turtle.color('yellow')
# turtle.speed('fastest')

# turtle.penup()
# turtle.goto(-200, 100)
# turtle.pendown()

# star(turtle, 360)

# turtle.hideturtle()
screen.mainloop()
