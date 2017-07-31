
def up():
    global direction
    direction = UP
    print('You pressed the up key!')
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x,y+10)
def down():
    global direction
    direction = DOWN
    print('you pressed the down key!')
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x,y-10)

def left():
    global direction
    direction = LEFT
    print('you pressed the left key!')
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x-10,y)

def right():
    global direction
    direction = RIGHT
    print('you pressed the right key!')
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x+10,y)

    


############################################

import turtle

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACEBAR = 'space'


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

direction = UP


turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()






 
turtle.mainloop()
