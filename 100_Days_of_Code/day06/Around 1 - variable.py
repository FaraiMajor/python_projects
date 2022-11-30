def turn_right():
    turn_left()
    turn_left()
    turn_left()


def counter_move():
    while front_is_clear():
        if not object_here():
            put()
            move()
        else:
            break
    turn_left()


repeat 4:
    counter_move()
counter_move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
# Link to game is below
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20apple&url=worlds%2Ftutorial_en%2Faround1c.json
################################################################
