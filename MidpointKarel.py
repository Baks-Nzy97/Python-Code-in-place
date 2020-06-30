from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
  This helps us find the midpoint
  first we check for the sizeof the world; ie 1x1 0r more
    """
    turn_left()
    if right_is_blocked():
        #takes care of a one by one world
        turn_right()
        put_beeper()
    else:
        ascend_diagonally()
        move_to_right_side_on_the_top()
        # Takes care of a 2x2 world
        if beepers_present():
            for i in range(2):
                turn_left()
                move()
            pick_beeper()
            turn_right()
        else:
            descend_diagonally()
            move_to_midpoint()
            pick_beepers()
        move_back_to_midpoint()


"""
pre-condition: Karel is facing east at the bottom of the world( street 1 avenue 1)
post-condition: Karel is facing east at the top of the world(east side)
"""

def ascend_diagonally():
    turn_right()
    while front_is_clear():
        put_beeper()
        move()
        turn_left()
        move()
        turn_right()
    put_beeper()

# Helps karel move down diagonally up to the place it meets a beeper(the midpoint)
def descend_diagonally():
        turn_left()
        move()
        while no_beepers_present():
            turn_right()
            move()
            if no_beepers_present():
                turn_left()
                move()

# leaves karel in a position to descend.
def move_to_right_side_on_the_top():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    move()

# Helps karel to move from the midpoint where it found a beeper to the bottom; the middle of the first street.
def move_to_midpoint():
    if facing_east():
        turn_right()
    while front_is_clear():
        move()
    turn_left()
    put_beeper()

# Removes the unnecessary beepers used to find the midpoint.
def pick_beepers():
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    while front_is_clear():
        pick_beeper()
        move()
        turn_left()
        move()
        turn_right()
    pick_beeper()

# it moves karel back to the midpoint after removing the beepers.
def move_back_to_midpoint():
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while no_beepers_present():
        move()

# Turns Karel 90 degrees to the right.
def turn_right():
    for i in range(3):
        turn_left()

#Turns Karel around 180 degrees.
def turn_around():
    for i in range(2):
        turn_left()




# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
    move()
