def turn_right():
    turn_left()
    turn_left()
    turn_left()


def L_shape():
    for i in range(3):
        move()
    turn_left()
    move()
    move()
    move()


def next_L():
    turn_right()
    move()
    turn_right()


repeat 3:
    L_shape()
    next_L()
L_shape()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
# Link to game is below
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20apple&url=worlds%2Ftutorial_en%2Faround1c.json
################################################################
