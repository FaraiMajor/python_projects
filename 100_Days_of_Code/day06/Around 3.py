def turn_right():
    turn_left()
    turn_left()
    turn_left()


put()
turn_left()
while True:
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()
    if wall_in_front():
        turn_left()
    if object_here():
        done()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
# Link to game is below
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20apple&url=worlds%2Ftutorial_en%2Faround1c.json
################################################################
