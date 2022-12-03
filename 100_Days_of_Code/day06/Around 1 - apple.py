def turn_right():
    turn_left()
    turn_left()
    turn_left()


while True:
    if front_is_clear():
        move()
    if object_here():
        take()
    if wall_in_front():
        turn_left()
    if at_goal():
        done()


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
# Link to game is below
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Around%201%20-%20apple&url=worlds%2Ftutorial_en%2Faround1c.json
################################################################

# farai mutukumira
