def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_n_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
count = 0
while count < 6:
    move_n_jump()
    count += 1
    
    